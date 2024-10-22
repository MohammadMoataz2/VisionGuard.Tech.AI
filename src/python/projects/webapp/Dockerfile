# Use the official Python image from the Docker Hub
FROM python:3.11

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install  -r requirements.txt

# Copy the entire app directory into the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "webapp/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
