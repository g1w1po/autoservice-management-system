from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Analytics Service",
    root_path="/analytics"
)

class ServiceRequest(BaseModel):
    id: int
    status: str
    price: float

@app.get("/")
def root():
    return {"service": "analytics-service", "status": "running"}

@app.post("/analytics")
def calculate_analytics(items: List[ServiceRequest]):
    total_requests = len(items)
    completed = len([item for item in items if item.status == "completed"])
    total_price = sum(item.price for item in items)
    return {
        "total_requests": total_requests,
        "completed_requests": completed,
        "total_price": total_price
    }
