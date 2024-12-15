import mlflow
import mlflow.pyfunc
from deepface_model import DeepFaceAnalysisModel
def train_model():
    # Simulate any training process if needed, or return None if unnecessary
    return None

if __name__ == "__main__":
    # Set MLflow tracking URI (default is local MLflow server)

    # Define experiment name
    experiment_name = "DeepFace_Analysis_Experiment"
    mlflow.set_experiment(experiment_name)



    mlflow.set_tracking_uri("http://localhost:5000")  # Replace with your MLflow server URI


    with mlflow.start_run() as run:
        # Log the DeepFace Analysis model
        model = DeepFaceAnalysisModel()

        # Save the model to MLflow
        mlflow.pyfunc.log_model(
            artifact_path="deepface_analysis_model",
            python_model=model,
            code_paths = ["./face_analyze/deepface_model.py"],
        )

        # Log optional parameters and metrics
        mlflow.log_param("model_type", "DeepFaceAnalysisModel")
        mlflow.log_metric("accuracy", 0.95)  # Replace with actual metric if calculated

        print(f"Model logged to MLflow with run ID: {run.info.run_id}")
