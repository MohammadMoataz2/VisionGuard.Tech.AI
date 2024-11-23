DOCKER_IMAGE_NAME_API = visionguard-tech-api
DOCKER_IMAGE_NAME_WEBAPP = visionguard-tech-webapp

DOCKER_TAG = 0.0.1
PANTS_BIN = pants
PANTS_BUILD_TARGET_API = src/python/projects/api:visionguard-tech-api
PANTS_BUILD_TARGET_WEBAPP = src/python/projects/webapp:visionguard-tech-webapp

DOCKER_USER_NAME = mohammadmoataz777
LOCAL_DEV_DIR = src/python/projects/api/.local_dev

.PHONY: all build-docker run-docker docker-run-local-dev clean generate-lockfile

all: generate-lockfile build-docker run-docker

# Generates lockfiles using Pants
generate-lockfile:
	$(PANTS_BIN) generate-lockfiles

# Builds the Docker image using Pants
build-docker: generate-lockfile
	$(PANTS_BIN) package $(PANTS_BUILD_TARGET_API)

#	$(PANTS_BIN) package $(PANTS_BUILD_TARGET_WEBAPP)


# Runs the Docker container exposing port 8000
run-docker: build-docker
	docker run -d --env-file .env  -p 8000:8000 --network host --name $(DOCKER_IMAGE_NAME_API) $(DOCKER_USER_NAME)/$(DOCKER_IMAGE_NAME_API):$(DOCKER_TAG)
#	docker run -d --env-file .env -p 8501:8501 --network host  --name $(DOCKER_IMAGE_NAME_WEBAPP) $(DOCKER_USER_NAME)/$(DOCKER_IMAGE_NAME_WEBAPP):$(DOCKER_TAG)

# Runs local dev environment, including MongoDB and Redis services
docker-run-local-dev:
	@cd $(LOCAL_DEV_DIR)/mongodb && $(MAKE) run
	@cd $(LOCAL_DEV_DIR)/redis && $(MAKE) run
	@cd $(LOCAL_DEV_DIR)/mlflow && $(MAKE) run

# Cleans up by removing the Docker container and image
clean:
	docker rm -f $(DOCKER_IMAGE_NAME_API) || true
	docker rmi -f $(DOCKER_IMAGE_NAME_API):$(DOCKER_TAG) || true

