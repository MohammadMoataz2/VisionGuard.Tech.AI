
from celery import Celery
import numpy as np
import requests
import cv2


# Configure Celery to use Redis as the broker
celery_app = Celery(
    'vision.tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task(name="vision.main.analyze_face_task")
def analyze_face_task(image_bytes: bytes, callback_url: str):
    """Analyze the image and send the result to the callback URL."""
    # Convert image bytes to a NumPy array
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if image is None:
        result = {"error": "Invalid image data"}
    else:
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Load Haar Cascade for face detection
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        face_detected = len(faces) > 0
        result = {"face_detected": face_detected}

    # Send the result to the callback endpoint

    response = requests.post(callback_url, json={"task_id": analyze_face_task.request.id, "result": result})

    if response.status_code == 200:
        print("Callback sent successfully.")
    else:
        print("Failed to send callback.")

