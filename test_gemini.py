import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env file")

print(f"Testing with GEMINI_API_KEY: {api_key[:4]}...")  # Masked output
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
try:
    response = model.generate_content("Test prompt: Hello, Gemini!")
    print("Success! Response:", response.text)
except Exception as e:
    print(f"Error: {str(e)}")