DOCKER_IMAGE_NAME = visionguard-tech-api
DOCKER_TAG = 0.0.2
PANTS_BIN = pants
PANTS_BUILD_TARGET = src/python/projects/api:visionguard-tech-api
DOCKER_USER_NAME = mohammadmoataz777
LOCAL_DEV_DIR = src/python/projects/api/.local_dev

.PHONY: all build-docker run-docker docker-run-local-dev clean generate-lockfile

all: generate-lockfile build-docker run-docker

# Generates lockfiles using Pants
generate-lockfile:
	$(PANTS_BIN) generate-lockfiles

# Builds the Docker image using Pants
build-docker: generate-lockfile
	$(PANTS_BIN) package $(PANTS_BUILD_TARGET)

# Runs the Docker container exposing port 8000
run-docker: build-docker
	docker run -d -p 8000:8000 --name $(DOCKER_IMAGE_NAME) $(DOCKER_USER_NAME)/$(DOCKER_IMAGE_NAME):$(DOCKER_TAG)

# Runs local dev environment, including MongoDB and Redis services
docker-run-local-dev:
	@cd $(LOCAL_DEV_DIR)/mongodb && $(MAKE) run
	@cd $(LOCAL_DEV_DIR)/redis && $(MAKE) run
	@cd $(LOCAL_DEV_DIR)/mlflow && $(MAKE) run

# Cleans up by removing the Docker container and image
clean:
	docker rm -f $(DOCKER_IMAGE_NAME) || true
	docker rmi -f $(DOCKER_IMAGE_NAME):$(DOCKER_TAG) || true

