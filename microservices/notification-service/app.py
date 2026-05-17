from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Notification Service")

class Notification(BaseModel):
    client_name: str
    phone: str
    status: str

@app.get("/")
def root():
    return {"service": "notification-service", "status": "running"}

@app.post("/notify")
def notify_client(data: Notification):
    message = f"Клиент {data.client_name}, статус вашей заявки: {data.status}"
    return {
        "message": "Уведомление сформировано",
        "phone": data.phone,
        "text": message
    }
