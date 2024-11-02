
import mlflow.pyfunc
from deepface import DeepFace
import numpy as np
import cv2
import base64
import pandas as pd

class DeepFaceAnalysisModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # Preload configurations for DeepFace if necessary
        self.actions = ["age", "gender", "emotion", "race"]

    def predict(self, context, model_input: pd.DataFrame):
        # Model input is expected to be a DataFrame with a column "image_bytes"
        image_bytes = model_input["image_bytes"].iloc[0]

        # Decode the base64 encoded image
        nparr = np.frombuffer(base64.b64decode(image_bytes), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Error: Could not decode the image.")

        # Perform face analysis using DeepFace
        analysis = DeepFace.analyze(img_path=image, actions=self.actions, enforce_detection=False)

        # Convert result to DataFrame format for compatibility
        return pd.DataFrame([analysis])
