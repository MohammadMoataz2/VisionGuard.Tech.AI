# Paths and Variables
MONGO_DOCKER_COMPOSE_PATH=/home/sheildsword2/Desktop/Work/DataEng/VisionGuard.Tech.AI.API_ALONE/api/.local_dev/mongodb/docker-compose.yml
API_PYTHON_SCRIPT=run_api.py

# Phony targets
.PHONY: all mongo up-mongo down-mongo logs-mongo up-api down-api logs-api run-api clean run-webapp

# Default action: bring up both MongoDB and the API
all: up-mongo up-api run-webapp

# MongoDB related tasks
up-mongo:
	docker-compose -f $(MONGO_DOCKER_COMPOSE_PATH) up -d

down-mongo:
	docker-compose -f $(MONGO_DOCKER_COMPOSE_PATH) down

logs-mongo:
	docker-compose -f $(MONGO_DOCKER_COMPOSE_PATH) logs -f

# API related tasks
up-api:
	python3 $(API_PYTHON_SCRIPT) &

down-api:
	# Placeholder for stopping the API, if applicable (e.g., stop FastAPI server or related services)
	# Example:
	# pkill -f 'python3 $(API_PYTHON_SCRIPT)'

logs-api:
	# Placeholder for viewing logs related to the API
	# Example: tail -f /path/to/api/logs.log

# Run the API script
run-api:
	python3 $(API_PYTHON_SCRIPT) &

run-webapp:
	cd webapp && reflex run &

run-mlflow:
	cd mlflow && sh serve_model.sh

# Clean up Docker containers, volumes, and networks
clean: down-mongo
	docker-compose -f $(MONGO_DOCKER_COMPOSE_PATH) rm -f
	docker volume prune -f
	docker network prune -f
