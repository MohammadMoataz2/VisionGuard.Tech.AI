import mlflow.pyfunc
from deepface import DeepFace
import pandas as pd
import base64
import numpy as np
import cv2

class DeepFaceAnalysisModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # Specify the actions for face analysis
        self.actions = ["age", "gender", "emotion", "race"]

    def predict(self, context, model_input: pd.DataFrame):
        # Expecting 'image_bytes' in the first row of the DataFrame
        image_bytes = model_input["image_bytes"].iloc[0]

        # Convert bytes to a NumPy array and decode the image
        nparr = np.frombuffer(base64.b64decode(image_bytes), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Error: Could not decode the image.")

        # Perform face analysis using DeepFace
        analysis = DeepFace.analyze(img_path=image, actions=self.actions, enforce_detection=False)

        # Extract relevant data into a structured response
        result = {
            "age": analysis[0]["age"],
            "gender": analysis[0]["gender"],
            "emotion": analysis[0]["dominant_emotion"],
            "race": analysis[0]["dominant_race"],
            "box": analysis[0].get("region", {})  # Coordinates of detected face
        }

        return pd.DataFrame([result])  # Return result as DataFrame
