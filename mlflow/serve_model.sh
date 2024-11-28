#!/bin/bash

export MLFLOW_TRACKING_URI=http://localhost:5000

mlflow ui &

# Serve the FaceDetectionModel
mlflow models serve -m "models:/FaceDetectionModel/1" --port 5004 -h 0.0.0.0

wait