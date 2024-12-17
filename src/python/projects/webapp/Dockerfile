# Use an official Python runtime as a parent image
FROM python:3.11-slim
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default environment variables for the ports
ENV WEBAPP_DOCKER_FRONTEND_PORT=3001
ENV WEBAPP_DOCKER_BACKEND_PORT=8001

# Expose the ports the app runs on
EXPOSE $WEBAPP_DOCKER_FRONTEND_PORT
EXPOSE $WEBAPP_DOCKER_BACKEND_PORT

# Command to run the application
CMD ["reflex", "run", "--frontend-port", "3001", "--backend-port", "8001"]