###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

file_map = {
    
    "clients.baml": "client<llm> CustomGemini {\r\n  provider google-ai\r\n  options {\r\n    model \"gemini-2.0-flash\"\r\n    generationConfig {\r\n      temperature 0\r\n    }\r\n    api_key env.GEMINI_API_KEY\r\n  }\r\n}\r\n\r\nretry_policy Exponential {\r\n  max_retries 2\r\n  strategy {\r\n    type exponential_backoff\r\n    delay_ms 300\r\n    multiplier 1.5\r\n    max_delay_ms 10000\r\n  }\r\n}",
    "generators.baml": "generator target {\n  output_type \"python/pydantic\"\n  output_dir \"../\"\n  version \"0.89.0\"\n  default_client_mode sync\n}",
    "resume.baml": "// Define the structured output for resume evaluation\r\nclass ResumeEvaluation {\r\n  score int @description(\"A score from 0 to 100 indicating how closely the candidate's resume matches the reference resume\")\r\n  reasoning string @description(\"A brief explanation justifying the score, max 100 words\")\r\n}\r\n\r\n// Define a function to evaluate resumes\r\nfunction EvaluateResumes(input_resume: string, reference_resume: string) -> ResumeEvaluation {\r\n  client CustomGemini\r\n  prompt #\"\r\n    You are an expert resume evaluator. Compare the following two resumes:\r\n\r\n    Candidate's Resume:\r\n    {{ input_resume }}\r\n\r\n    Reference Resume:\r\n    {{ reference_resume }}\r\n\r\n    Provide a score from 0 to 100 indicating how closely the candidate's resume matches the reference resume.\r\n    Also provide a brief reasoning (max 100 words).\r\n\r\n    {{ ctx.output_format }}\r\n  \"#\r\n}",
}

def get_baml_files():
    return file_map