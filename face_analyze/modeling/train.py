import mlflow
import mlflow.pyfunc
from mlflow_model import DeepFaceAnalysisModel


def train_model(data):
    # Simulate training logic here if needed
    return None  # Return your trained model if applicable


if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")  # Change to your MLflow server if needed

    # Create or set the DeepFace analysis experiment
    df_experiment_name = "DeepFace_Analysis_Experiment"
    mlflow.set_experiment(df_experiment_name)

    with mlflow.start_run() as df_run:
        # Log the DeepFace Analysis model
        df_model = DeepFaceAnalysisModel()

        # Log the model to MLflow
        df_model_uri = mlflow.pyfunc.log_model(
            "deepface_analysis_model",
            python_model=df_model
        )

        # Optionally log additional parameters or metrics
        mlflow.log_param("model_type", "DeepFace")
        mlflow.log_metric("accuracy", 0.95)  # Replace with actual metric if available

        print(f"Model logged to MLflow with URI: {df_model_uri}")
