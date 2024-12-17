.PHONY: build_run_api

# Target to build and run the API
build_run_api:
	chmod +x src/python/projects/api/build_and_run.sh && \
	cd src/python/projects/api && ./build_and_run.sh