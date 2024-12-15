# mlflow/Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /mlflow

# Install dependencies
RUN pip install mlflow pymysql boto3 psycopg2-binary cryptography

# Add this line in your Dockerfile

# Set environment variables
ENV MLFLOW_TRACKING_URI=http://0.0.0.0:5000
ENV MLFLOW_S3_ENDPOINT_URL=${MLFLOW_S3_ENDPOINT_URL}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

EXPOSE 5000

# Command to run the MLflow server
CMD ["mlflow", "server", "--default-artifact-root", "s3://${MINIO_BUCKET_NAME}", "--host", "0.0.0.0", "--port", "5000"]
