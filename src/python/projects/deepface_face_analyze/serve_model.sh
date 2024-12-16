#!/bin/bash

# Load environment variables from the .env file
if [ -f .env ]; then
  export $(cat .env | xargs)
else
  echo ".env file not found. Please create one with the required variables."
  exit 1
fi

# Check if required environment variables are set
if [[ -z "$DOCKER_IMAGE_TAG" ]] || [[ -z "$DOCKER_IMAGE_VERSION" ]]; then
  echo "DOCKER_IMAGE_TAG or DOCKER_IMAGE_VERSION is not set in the .env file."
  exit 1
fi

# Combine tag and version
FULL_TAG="${DOCKER_IMAGE_TAG}:${DOCKER_IMAGE_VERSION}"

# Build the Docker image
echo "Building Docker image with tag: $FULL_TAG..."
docker build -t "$FULL_TAG" .

# Check if the build was successful
if [ $? -ne 0 ]; then
  echo "Docker build failed."
  exit 1
fi

# Run the Docker container
# Run the Docker container
echo "Running Docker container from image: $FULL_TAG..."
docker run --network host --env-file .env --name deepface_analysis_container "$FULL_TAG"
