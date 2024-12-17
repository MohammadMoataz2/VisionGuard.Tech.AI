#!/bin/bash


set -o allexport
source .env
set +o allexport

# Define variables for container and image names
IMAGE_NAME="visionguard-webapp"
CONTAINER_NAME="visionguard-webapp-container"
WEBAPP_DOCKER_FRONTEND_PORT=${WEBAPP_DOCKER_FRONTEND_PORT:-3001}
WEBAPP_DOCKER_BACKEND_PORT=${WEBAPP_DOCKER_BACKEND_PORT:-8001}

# Stop and remove any existing containers using the same name
echo "Stopping and removing any existing container..."
docker stop $CONTAINER_NAME || true
docker rm $CONTAINER_NAME || true

# Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

echo "Opening the browser with the web app URL: $WEBAPP_CONN_STR"

# Open the browser (works on Linux and macOS; modify for Windows if needed)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open $WEBAPP_CONN_STR
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open $WEBAPP_CONN_STR
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
    start $WEBAPP_CONN_STR
else
    echo "Unsupported OS, please open the browser manually."
fi

# Run the Docker container
echo "Running the Docker container..."
docker run   --env-file .env --network host -p $WEBAPP_DOCKER_FRONTEND_PORT:$WEBAPP_DOCKER_FRONTEND_PORT -p $WEBAPP_DOCKER_BACKEND_PORT:$WEBAPP_DOCKER_BACKEND_PORT --name $CONTAINER_NAME $IMAGE_NAME


