from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Event(BaseModel):
    eventType: str
    details: dict
    timestamp: int

@app.post("/report-event")
async def report_event(event: Event):
    # For now, just log to console (later: save to DB)
    readable_time = datetime.datetime.fromtimestamp(event.timestamp / 1000)
    print(f"[{readable_time}] Event received: {event.eventType} | Details: {event.details}")
    return {"status": "logged"}


