# Resume Evaluator API

A FastAPI-based backend for evaluating candidate resumes against a reference resume using Google Gemini LLM via BAML. Upload two PDF resumes and receive a structured score and reasoning.

![image](https://github.com/user-attachments/assets/a03dc085-e4ce-4007-a9b3-c5c2121d5cfb)


---

## Features

- **PDF Resume Upload:** Upload candidate and reference resumes as PDF files.
- **Text Extraction:** Extracts text from PDFs using `pdfplumber`.
- **LLM Evaluation:** Uses Google Gemini (via BAML) to compare resumes and generate a score (0–100) and reasoning.
- **REST API:** Simple `/api/v1/evaluate` endpoint for integration.
- **Environment-based Configuration:** API keys loaded from `.env`.
- **Error Handling:** Validates file types and handles LLM/API errors gracefully.

---

## Project Structure

```
resume-eval/
│
├── app/
│   ├── [`app/__init__.py`](app/__init__.py )
│   ├── [`app/main.py`](app/main.py )                # FastAPI app entrypoint
│   ├── core/
│   │   └── [`app/core/config.py`](app/core/config.py )          # Loads environment variables
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── [`app/api/v1/endpoints/evaluate.py`](app/api/v1/endpoints/evaluate.py ) # /evaluate endpoint
│   ├── services/
│   │   └── [`app/services/evaluator.py`](app/services/evaluator.py )       # (Unused) Async evaluation service
│   └── utils/
│       ├── [`app/utils/pdf_reader.py`](app/utils/pdf_reader.py )      # PDF text extraction
│       └── [`app/utils/file_handler.py`](app/utils/file_handler.py )    # (Unused) File saving utility
│
├── baml_client/               # Auto-generated BAML Python client
│   └── ...                    # (Do not edit manually)
│
├── baml_src/
│   ├── [`baml_src/clients.baml`](baml_src/clients.baml )           # BAML Gemini client definition
│   ├── [`baml_src/generators.baml`](baml_src/generators.baml )        # BAML codegen config
│   └── [`baml_src/resume.baml`](baml_src/resume.baml )            # BAML function for resume evaluation
│
├── .env                       # Contains GEMINI_API_KEY
├── [`requirements.txt`](requirements.txt )           # Python dependencies
├── [`README.md`](README.md )                  # This file
├── [`test_baml_env.py`](test_baml_env.py )           # Test: BAML env and function
├── [`test_gemini.py`](test_gemini.py )             # Test: Gemini API direct call
└── .gitignore
```

---

## Setup

### 1. Clone the Repository

```sh
git clone <repo-url>
cd resume-eval
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Add these lines to `requirements.txt` if not present:

```
fastapi
uvicorn
python-dotenv
pdfplumber
google-generativeai
baml
```

Then install:

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your-google-gemini-api-key
```

Replace `your-google-gemini-api-key` with your actual Gemini API key.

---

## BAML Code Generation

If you modify any `.baml` files in `baml_src/`, regenerate the Python client:

```sh
baml generate
```

This updates the `baml_client/` directory.

---

## Running the API

Start the FastAPI server:

```sh
uvicorn app.main:app --reload
```

- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/health](http://localhost:8000/health)

---

## API Usage

### `POST /api/v1/evaluate`

**Description:**  
Upload two PDF files: a candidate's resume and a reference resume. Returns a score and reasoning.

**Request:**

- `input_resume`: PDF file (candidate)
- `reference_resume`: PDF file (reference)

**Example with `curl`:**

```sh
curl -X POST "http://localhost:8000/api/v1/evaluate" \
  -F "input_resume=@candidate.pdf" \
  -F "reference_resume=@reference.pdf"
```

**Response:**

```json
{
  "score": 87,
  "reasoning": "The candidate's resume closely matches the reference in skills and experience, but lacks project management exposure."
}
```

---

## Testing

### Test BAML Environment

```sh
python test_baml_env.py
```

### Test Gemini API Directly

```sh
python test_gemini.py
```

---

## Implementation Details

- **PDF Extraction:** `extract_text_from_pdf` uses `pdfplumber` to extract text from each page.
- **BAML Client:** `b.EvaluateResumes` is called with extracted text.
- **API Endpoint:** `evaluate_resumes` handles file validation, extraction, and response formatting.
- **Configuration:** `Settings` loads the Gemini API key from `.env`.

---

## Troubleshooting

- **Missing API Key:** Ensure `.env` exists and contains `GEMINI_API_KEY`.
- **PDF Extraction Issues:** Check that uploaded files are valid PDFs.
- **BAML Errors:** Regenerate the client if `.baml` files change (`baml generate`).

---

## License

MIT License

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Gemini](https://ai.google.dev/)
- [BAML](https://docs.boundaryml.com/home)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
