# Load environment variables from .env file
include .env
export $(shell sed 's/=.*//' .env)


run:
	python face_analyze/train.py