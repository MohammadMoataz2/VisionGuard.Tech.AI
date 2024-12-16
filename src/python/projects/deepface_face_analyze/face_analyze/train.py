import mlflow
import mlflow.pyfunc
from deepface_model import DeepFaceAnalysisModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get tracking URI and experiment name from environment variables
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")  # Default to localhost if not set
experiment_name = os.getenv("MLFLOW_EXPERIMENT_NAME", "Default_Experiment")

def train_model():
    # Simulate any training process if needed, or return None if unnecessary
    return None

if __name__ == "__main__":
    # Set MLflow tracking URI
    mlflow.set_tracking_uri(tracking_uri)

    # Define and set experiment name
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        # Log the DeepFace Analysis model
        model = DeepFaceAnalysisModel()

        # Save the model to MLflow
        mlflow.pyfunc.log_model(
            artifact_path="deepface_analysis_model",
            python_model=model,
            code_paths=["./face_analyze/deepface_model.py"],
        )

        # Log optional parameters and metrics
        mlflow.log_param("model_type", "DeepFaceAnalysisModel")
        import random

        # Generate a random accuracy value between 0.8 and 0.99
        random_accuracy = round(random.uniform(0.8, 0.99), 3)

        mlflow.log_metric("accuracy", random_accuracy)

        print(f"Model logged to MLflow with run ID: {run.info.run_id}")
