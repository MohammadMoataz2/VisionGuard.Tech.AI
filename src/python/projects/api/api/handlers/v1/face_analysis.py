from fastapi import APIRouter
router = APIRouter()


from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from typing import Dict
from vision.main import analyze_face_task


# Temporary storage for results (in a production system, use a database)
results_store: Dict[str, dict] = {}

@router.post("/analyze-face/")
async def analyze_face(

        file: UploadFile = File(...)):
    """API to receive a PNG image and send it to Celery."""
    if file.content_type != "image/png":
        raise HTTPException(status_code=400, detail="Only PNG files are supported.")

    # Read the image bytes from the file
    image_bytes = await file.read()

    # Prepare the callback URL (local FastAPI callback endpoint)
    callback_url = "http://localhost:5000"

    # Register the Celery task with the image bytes and callback URL
    analyze_face_task.delay(image_bytes, callback_url)

    return {"message": "Task registered successfully"}

@router.post("/callback/")
async def callback(result: dict):
    """API endpoint to receive the result from Celery."""
    # Store the result in memory (for simplicity)
    results_store["last_result"] = result
    return {"message": "Result received successfully"}

@router.get("/result/")
async def get_result():
    """API to retrieve the latest analysis result."""
    if "last_result" not in results_store:
        raise HTTPException(status_code=404, detail="No result available.")
    return results_store["last_result"]
