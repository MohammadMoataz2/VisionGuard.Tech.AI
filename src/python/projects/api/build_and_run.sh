#!/bin/bash

# Load environment variables from .env file
set -o allexport
source .env
set +o allexport

# Check if all necessary environment variables are set
if [ -z "$DOCKER_IMAGE_NAME" ] || [ -z "$DOCKER_CONTAINER_NAME" ] || [ -z "$DOCKER_TAG" ]; then
  echo "Error: One or more Docker environment variables are not set in the .env file."
  exit 1
fi

# Build the Docker image
echo "Building Docker image: $DOCKER_IMAGE_NAME:$DOCKER_TAG"
docker build -t "$DOCKER_IMAGE_NAME:$DOCKER_TAG" .

# Remove any existing container with the same name
echo "Stopping and removing existing container (if any)..."
docker rm -f "$DOCKER_CONTAINER_NAME" || true

# Run the Docker container
echo "Running Docker container: $DOCKER_CONTAINER_NAME"
docker run --env-file .env --name "$DOCKER_CONTAINER_NAME" --network host  "$DOCKER_IMAGE_NAME:$DOCKER_TAG"

# Output container status
docker ps -a | grep "$DOCKER_CONTAINER_NAME"
