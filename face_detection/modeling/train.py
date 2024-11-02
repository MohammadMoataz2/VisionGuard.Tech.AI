import mlflow
import mlflow.pyfunc
from mlflow_model import CVFaceDetectionModel  # Ensure the path is correct


def train_model(data):
    # Simulate training logic here if applicable
    # For a face detection model using a pre-trained classifier, training might not be necessary.

    # Here we would typically train a model, but since we are using a Haar Cascade,
    # we might just return a placeholder or pre-trained model.

    return None  # Return your trained model if applicable


if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")  # Change to your MLflow server if needed

    # Create or set the CV Face Detection experiment
    cv_experiment_name = "CV_Face_Detection_Experiment"
    mlflow.set_experiment(cv_experiment_name)

    with mlflow.start_run() as cv_run:
        # Log the CV Face Detection model
        cv_model = CVFaceDetectionModel()

        # Log the model to MLflow
        cv_model_uri = mlflow.pyfunc.log_model(
            "cv_face_detection_model",
            python_model=cv_model
        )

        # Optionally log additional parameters or metrics
        mlflow.log_param("model_type", "Haar Cascade")
        mlflow.log_metric("accuracy", 0.95)  # Replace with actual metric if available

        print(f"Model logged to MLflow with URI: {cv_model_uri}")
