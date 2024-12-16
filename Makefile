# Makefile

# Path to the component script
COMPONENT_SCRIPT_PATH=src/python/projects/components/component_up.sh

# Path to the serve model script
SERVE_MODEL_SCRIPT_PATH=src/python/projects/deepface_face_analyze/serve_model.sh

# Target to run the component script
component:
	@echo "Running component script..."
	@bash $(COMPONENT_SCRIPT_PATH)

# Target to run the serve model script
serve_model:
	@echo "Running serve model script..."
	@bash $(SERVE_MODEL_SCRIPT_PATH)

# Target to run both scripts
all: component serve_model
	@echo "Both component and serve model scripts are executed."
