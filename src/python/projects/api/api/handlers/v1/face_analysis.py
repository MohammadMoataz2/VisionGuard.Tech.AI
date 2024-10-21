from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Form
from vision.main import analyze_face_task
from pydantic import BaseModel, Json

router = APIRouter()


class CallbackInfo(BaseModel):
    callback_url: str  # Callback URL
    other_info: str
    immediately: bool


@router.post("/analyze-face/")
async def analyze_face(
        callback_info: Json[CallbackInfo] = None,
        file: UploadFile = File(...),

        ):

    image_bytes = await file.read()

    if callback_info.immediately == True:
        return analyze_face_task(image_bytes, callback_info)


    analyze_face_task.delay(image_bytes, callback_info)

    return {"message": "Task registered successfully"}




