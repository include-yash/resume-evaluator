from fastapi import FastAPI
from app.api.v1.endpoints import evaluate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resume Evaluator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(evaluate.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Welcome to the Resume Evaluator API. Use /api/v1/evaluate to evaluate resumes."}