# minio/docker-compose.yml

FROM minio/minio:latest

# Set environment variables for MinIO
ENV MINIO_ROOT_USER=${MINIO_ROOT_USER}
ENV MINIO_ROOT_PASSWORD=${MINIO_ROOT_PASSWORD}

# Command to start MinIO server
CMD ["server", "/data"]

EXPOSE 9000 9001
