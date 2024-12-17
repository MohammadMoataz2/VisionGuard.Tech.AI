.PHONY: build_run_component build_run_api build_run_webapp run

# Target to build and run the API
build_run_api:
	chmod +x src/python/projects/api/build_and_run.sh && \
	cd src/python/projects/api && ./build_and_run.sh

# Target to build and run the web application
build_run_webapp:
	chmod +x src/python/projects/webapp/build_and_run.sh && \
	cd src/python/projects/webapp && ./build_and_run.sh

build_run_component:
	chmod +x src/python/projects/components/build_and_run.sh && \
	cd src/python/projects/components && ./build_and_run.sh

# Target to build and run both the API and web application in parallel
run:
	@echo "Running both API and Web Application in parallel..."
	# Run both in parallel using `&` operator
	$(MAKE) build_run_component &
	$(MAKE) build_run_api &
	$(MAKE) build_run_webapp &

	wait
