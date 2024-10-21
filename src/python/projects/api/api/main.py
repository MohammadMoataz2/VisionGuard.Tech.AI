from fastapi import FastAPI
from visionguard.common.doc import a
from api.core import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
print(a)

# CORS configuration
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
    # Allow CORS requests from this origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

from .handlers import v1

app.include_router(v1.api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Hello, FastAPI!{a}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "qr": q}

