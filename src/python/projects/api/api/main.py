from fastapi import FastAPI
from visionguard.common.doc import a
app = FastAPI()
print(a)

@app.get("/")
def read_root():
    return {"message": f"Hello, FastAPI!{a}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

