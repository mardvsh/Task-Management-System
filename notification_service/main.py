from fastapi import FastAPI
import uvicorn
from notification_service.notification import send_notification

app = FastAPI()

@app.post("/notify/")
async def notify(user_id: int, message: str):
    send_notification(user_id, message)
    return {"message": "Notification sent"}

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8003)
