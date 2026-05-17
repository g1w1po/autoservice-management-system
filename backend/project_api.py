from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Autoservice Main API",
    root_path="/api"
)

class RequestData(BaseModel):
    client_name: str
    car_model: str
    problem: str
    status: str

requests_storage = []

@app.get("/")
def root():
    return {"message": "Autoservice main API is running"}

@app.post("/requests")
def create_request(data: RequestData):
    requests_storage.append(data.dict())
    return {
        "message": "Заявка принята основным сервисом",
        "request": data
    }

@app.get("/requests")
def get_requests():
    return {
        "count": len(requests_storage),
        "items": requests_storage
    }
