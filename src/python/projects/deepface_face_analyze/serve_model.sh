#!/bin/bash

# Source the .env file to load environment variables
source .env

# Set the MLFLOW_TRACKING_URI from the .env file
export MLFLOW_TRACKING_URI=http://localhost:$MLFLOW_PORT

# Serve the FaceDetectionModel using the port from the .env file
mlflow models serve -m "models:/DeepFaceAnalyzeModel/1" --port $MLFLOW_MODEL_PORT &
