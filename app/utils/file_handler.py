import os
from fastapi import UploadFile
from uuid import uuid4

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_upload_file(upload_file: UploadFile) -> str:
    """Save uploaded file to temp folder and return the saved path"""
    ext = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid4().hex}{ext}"
    file_path = os.path.join(TEMP_DIR, unique_filename)

    with open(file_path, "wb") as f:
        content = upload_file.file.read()
        f.write(content)
    
    return file_path
