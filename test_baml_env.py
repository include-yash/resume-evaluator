import os
from dotenv import load_dotenv
from baml_client import b

print("Starting test_baml_env.py")  # Debug line

load_dotenv()  # Load .env file

def test_baml_env():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment")
    else:
        print(f"BAML sees GEMINI_API_KEY: {api_key[:4]}...")

    try:
        result = b.EvaluateResumes(
            input_resume="Test resume",
            reference_resume="Reference resume"
        )
        print("Success! Result:", {"score": result.score, "reasoning": result.reasoning})
    except Exception as e:
        print(f"BAML error: {str(e)}")

if __name__ == "__main__":
    test_baml_env()
