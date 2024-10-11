.PHONY: all help run

all: help

help:
	@echo "run 'make run' for running mongoDB and admin web'"

run:
	@sensible-browser http://localhost:6003
	@docker compose -f docker-compose.yml up -d
