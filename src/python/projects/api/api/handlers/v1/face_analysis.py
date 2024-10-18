from fastapi import APIRouter
router = APIRouter()


from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Form
from typing import Dict
from vision.main import analyze_face_task
from pydantic import BaseModel, Json


class CallbackInfo(BaseModel):
    callback_url: str  # Callback URL
    other_info: str    # Additional info as needed


# Temporary storage for results (in a production system, use a database)
results_store: Dict[str, dict] = {}

@router.post("/analyze-face/")
async def analyze_face(
        callback_info: Json[CallbackInfo] = None,
        file: UploadFile = File(...),

        ):


    """API to receive a PNG image and send it to Celery."""

    # Read the image bytes from the file
    image_bytes = await file.read()

    # Prepare the callback URL (local FastAPI callback endpoint)
    callback_url = callback_info.callback_url

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
