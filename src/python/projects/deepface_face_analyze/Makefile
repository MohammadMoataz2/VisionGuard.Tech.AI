# Load environment variables from .env file
include .env
export $(shell sed 's/=.*//' .env)

# Define the MLflow server start command
#MLFLOW_CMD=mlflow server --backend-store-uri $(MLFLOW_BACKEND_URI) --default-artifact-root $(MLFLOW_ARTIFACT_URI) --host 0.0.0.0 --port $(MLFLOW_PORT)

MLFLOW_CMD=mlflow server --host 0.0.0.0 --port $(MLFLOW_PORT)
# Target to start MLflow server and then run training
run:
	@echo "Starting MLflow server on port $(MLFLOW_PORT)..."
	$(MLFLOW_CMD) &
	@echo "Running training script..."
	python face_analyze/train.py