import cv2
import numpy as np
import mlflow.pyfunc


class CVFaceDetectionModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # Load the Haar Cascade model for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def predict(self, context, model_input):
        # Expecting 'image_bytes' in the input dictionary
        image_bytes = model_input["image_bytes"][0]

        # Convert bytes to a NumPy array and decode the image
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Error: Could not decode the image.")

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Prepare the response with detection status and coordinates
        result = {
            "face": len(faces) > 0,
            "coordinates": [{"x": int(x), "y": int(y), "width": int(w), "height": int(h)} for (x, y, w, h) in faces]
        }

        return result
