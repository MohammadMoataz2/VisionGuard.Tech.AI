from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Form
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
        result = requests.post("http://localhost:5000/process-data", json={"data": data})
        return


    return {"message": "Task registered successfully"}




