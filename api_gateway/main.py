from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# Прокси маршруты к микросервисам
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    # Логика проксирования запроса к Task Service
    pass

@app.post("/tasks/")
async def create_task(task: dict):
    # Логика проксирования запроса к Task Service
    pass


#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
