import sys
import os
import uvicorn
import subprocess
import signal

# 1. Add the "api/" folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
libs_dir = os.path.join(current_dir, "libs/common/")
sys.path.insert(0, libs_dir)

api_dir = os.path.join(current_dir, "projects/api/")
sys.path.insert(0, api_dir)

vision_dir = os.path.join(current_dir, "projects/vision/")
sys.path.insert(0, vision_dir)

# 2. Function to start the Celery worker
def start_celery_worker():
    """Start the Celery worker."""
    celery_cmd = [
        "celery",
        "-A", "projects.vision.vision.main",
        "worker",
        "--loglevel=info"
    ]
    return subprocess.Popen(celery_cmd)

# 3. Run the FastAPI server using Uvicorn
if __name__ == "__main__":
    # Start the Celery worker
    celery_process = start_celery_worker()

    try:
        # Run the FastAPI app
        uvicorn.run("projects.api.api.main:app", host="0.0.0.0", port=8011, reload=True)
    except KeyboardInterrupt:
        print("Shutting down FastAPI server...")
    finally:
        # Terminate the Celery worker when the FastAPI server is stopped
        os.kill(celery_process.pid, signal.SIGTERM)
        print("Celery worker terminated.")
