import sys





import uvicorn


if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8010, reload=True)