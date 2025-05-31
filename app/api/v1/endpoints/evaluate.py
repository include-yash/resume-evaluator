from fastapi import APIRouter, File, UploadFile, HTTPException
from app.utils.pdf_reader import extract_text_from_pdf
from baml_client import b
from baml_client.types import ResumeEvaluation

router = APIRouter()

@router.post("/evaluate")
async def evaluate_resumes(
    input_resume: UploadFile = File(...),
    reference_resume: UploadFile = File(...)
):
    # Validate PDFs
    if input_resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Input resume must be a PDF file.")
    if reference_resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Reference resume must be a PDF file.")
    
    # Extract text from uploaded PDFs
    input_text = await extract_text_from_pdf(input_resume)
    reference_text = await extract_text_from_pdf(reference_resume)

    # Call BAML LLM function synchronously (b.EvaluateResumes is blocking)
    # If you want async, you can run it in a threadpool but simple sync is okay for now
    result: ResumeEvaluation = b.EvaluateResumes(
        input_resume=input_text, 
        reference_resume=reference_text
    )
    
    # Return as JSON
    return {
        "score": result.score,
        "reasoning": result.reasoning,
    }
