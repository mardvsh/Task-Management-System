from fastapi import FastAPI, File, UploadFile
import uvicorn
from file_attachment_service.file_handler import save_file

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = save_file(file)
    return {"file_path": file_path}

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8004)
