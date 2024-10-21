from celery import Celery
import numpy as np
import requests
import cv2
import logging
from pydantic import BaseModel
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Celery to use Redis as the broker
celery_app = Celery(
    'vision.tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

class CallbackInfo(BaseModel):
    callback_url: str  # Callback URL
    other_info: str
    immediately: bool
    # Additional info as needed



@celery_app.task(name="vision.main.analyze_face_task")
def analyze_face_task(image_bytes: bytes, callback_info):
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



    if callback_info.immediately == True:
        return result

    # Send the result to the callback endpoint
    logger.info(f"Sending callback to {callback_info.callback_info} with result: {result}")

    try:
        response = requests.post(callback_info.callback_url, json={"task_id": analyze_face_task.request.id, "result": face_detected})

    except:
       print("here")