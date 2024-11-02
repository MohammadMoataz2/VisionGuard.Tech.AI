import mlflow
import mlflow.pyfunc
from models.cv_face_detection_model import CVFaceDetectionModel
from models.deep_face_analysis_model import DeepFaceAnalysisModel


def main():
    # Set tracking URI if needed
    mlflow.set_tracking_uri("http://localhost:5000")  # Change to your MLflow server if needed

    # Create or set the CV Face Detection experiment
    cv_experiment_name = "CV_Face_Detection_Experiment"
    mlflow.set_experiment(cv_experiment_name)

    with mlflow.start_run() as cv_run:
        # Log the CV Face Detection model
        cv_model = CVFaceDetectionModel()
        cv_model_uri = mlflow.pyfunc.log_model("cv_face_detection_model", python_model=cv_model)

        print(f"Logged CV Face Detection model at: {cv_model_uri}")

    # Create or set the DeepFace Analysis experiment
    deepface_experiment_name = "DeepFace_Analysis_Experiment"
    mlflow.set_experiment(deepface_experiment_name)

    with mlflow.start_run() as deepface_run:
        # Log the DeepFace Analysis model
        deepface_model = DeepFaceAnalysisModel()
        deepface_model_uri = mlflow.pyfunc.log_model("deep_face_analysis_model", python_model=deepface_model)

        print(f"Logged DeepFace Analysis model at: {deepface_model_uri}")


if __name__ == "__main__":
    main()
