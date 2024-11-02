import mlflow
import mlflow.pyfunc
from deepface import DeepFace
import numpy as np
import cv2
import base64
class DeepFaceAnalysisModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # Preload any models or configurations for DeepFace if necessary
        self.actions = ["age", "gender", "emotion", "race"]

    def predict(self, context, model_input):
        # Expecting 'image_bytes' in the input dictionary
        image_bytes = model_input["instances"][0]["image_bytes"]

        # Decode the base64 encoded image
        nparr = np.frombuffer(base64.b64decode(image_bytes), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Error: Could not decode the image.")

        # Perform face analysis using DeepFace
        analysis = DeepFace.analyze(img_path=image, actions=self.actions, enforce_detection=False)

        # Extract relevant data
        result = {
            "age": analysis["age"],
            "gender": analysis["gender"],
            "emotion": analysis["dominant_emotion"],
            "race": analysis["dominant_race"],
            "box": analysis.get("region", {})  # Coordinates of detected face
        }

        return result
