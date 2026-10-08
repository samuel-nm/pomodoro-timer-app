from config import STAGES
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Pomodoro Timer API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Pomodoro Timer API is running"}

@app.get("/stages")
def get_stages():
    return {"stages": STAGES}

@app.get("/stages/{stage_id}")
def get_stage(stage_id: str):
    if stage_id not in STAGES:
        raise HTTPException(status_code=404, detail="Stage not found")
    return STAGES[stage_id]