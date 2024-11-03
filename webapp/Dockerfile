# Use an official Python base image with OpenCV compatibility
FROM python:3.11-slim

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the requirements.txt file (assumes you have it in your project)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "webapp/main.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false", "--server.headless=true"]
