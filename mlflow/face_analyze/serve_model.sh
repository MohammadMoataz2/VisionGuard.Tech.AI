#!/bin/bash
export MLFLOW_TRACKING_URI=http://localhost:5000
# Serve the FaceDetectionModel
mlflow models serve -m "models:/FaceDetectionModel/1" --port 5003 &

# Serve the DeepFaceAnalyzeModel
mlflow models serve -m "models:/DeepFaceAnalyzeModel/1" --port 5004 &

# Wait for all background processes to finish
wait
