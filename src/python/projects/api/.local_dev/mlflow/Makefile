.PHONY: all help run

all: help

help:
	@echo "run 'make run' for running mlflow and admin web'"

run:
	@sensible-browser http://localhost:5000
	@docker compose -f docker-compose.yml up -d
