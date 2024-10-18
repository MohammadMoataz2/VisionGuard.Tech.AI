from fastapi import FastAPI
from visionguard.common.doc import a
from api.core import settings
app = FastAPI()
print(a)



from .handlers import v1

app.include_router(v1.api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Hello, FastAPI!{a}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "qr": q}

