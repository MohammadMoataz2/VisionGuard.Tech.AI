import sys



vision_guard_path = "/home/sheildsword2/Desktop/Work/DataEng/VisionGuard.Tech.AI.API_ALONE/src/python/libs/common"
projects_path = "/home/sheildsword2/Desktop/Work/DataEng/VisionGuard.Tech.AI.API_ALONE/src/python/projects"

sys.path.insert(0,vision_guard_path)
sys.path.insert(0,projects_path)




import uvicorn


if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8010, reload=True)
