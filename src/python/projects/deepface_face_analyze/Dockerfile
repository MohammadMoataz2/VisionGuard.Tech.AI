# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libbz2-dev \
    libssl-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libffi-dev \
    liblzma-dev \
    ffmpeg \
    libsm6 \
    libxext6 && \
    pip install --no-cache-dir virtualenv && \
    curl https://pyenv.run | bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV MLFLOW_TRACKING_URI=http://localhost:5000
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="/root/.pyenv/bin:/root/.pyenv/shims:$PATH"

EXPOSE 5004

RUN bash -c "source ~/.bashrc && pyenv install 3.11.11"

RUN pip install mlflow virtualenv

CMD ["bash", "-c", "source ~/.bashrc && mlflow models serve -m 'models:/DeepFaceAnalyzeModel/1' --port 5004"]
