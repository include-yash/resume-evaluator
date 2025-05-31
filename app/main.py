from fastapi import FastAPI
from app.api.v1.endpoints import evaluate

app = FastAPI(title="Resume Evaluator API")

app.include_router(evaluate.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Welcome to the Resume Evaluator API"}
