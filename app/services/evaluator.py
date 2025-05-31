from baml_client import b
from baml_client.types import ResumeEvaluation

async def evaluate_resumes_with_gemini(input_text: str, reference_text: str) -> dict:
    try:
        # Call the BAML EvaluateResumes function
        result = b.EvaluateResumes(input_resume=input_text, reference_resume=reference_text)
        
        # Convert the ResumeEvaluation Pydantic model to a dict for API response
        return {
            "score": result.score,
            "reasoning": result.reasoning
        }
    except Exception as e:
        raise ValueError(f"BAML evaluation failed: {str(e)}")