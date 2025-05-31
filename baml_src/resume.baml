// Define the structured output for resume evaluation
class ResumeEvaluation {
  score int @description("A score from 0 to 100 indicating how closely the candidate's resume matches the reference resume")
  reasoning string @description("A brief explanation justifying the score, max 100 words")
}

// Define a function to evaluate resumes
function EvaluateResumes(input_resume: string, reference_resume: string) -> ResumeEvaluation {
  client CustomGemini
  prompt #"
    You are an expert resume evaluator. Compare the following two resumes:

    Candidate's Resume:
    {{ input_resume }}

    Reference Resume:
    {{ reference_resume }}

    Provide a score from 0 to 100 indicating how closely the candidate's resume matches the reference resume.
    Also provide a brief reasoning (max 100 words).

    {{ ctx.output_format }}
  "#
}