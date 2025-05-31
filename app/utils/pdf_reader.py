import pdfplumber
from fastapi import UploadFile
from io import BytesIO

async def extract_text_from_pdf(file: UploadFile) -> str:
    # Read file content into bytes
    contents = await file.read()
    with pdfplumber.open(BytesIO(contents)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()
