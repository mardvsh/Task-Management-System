from fastapi import FastAPI
import uvicorn
from tag_service.tag_handler import add_tag, get_tags

app = FastAPI()

@app.post("/tags/")
async def create_tag(tag: str):
    add_tag(tag)
    return {"message": "Tag added"}

@app.get("/tags/")
async def read_tags():
    tags = get_tags()
    return {"tags": tags}

#if __name__ == "__main__":
 #   uvicorn.run(app, host="0.0.0.0", port=8005)
