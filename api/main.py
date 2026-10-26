from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.engine import analyze

app = FastAPI(title="ReviewRadar AI", version="1.0.0")

class ReviewRequest(BaseModel):
    review: str = Field(min_length=1, max_length=5000)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def review(payload: ReviewRequest):
    try:
        return analyze(payload.review)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
