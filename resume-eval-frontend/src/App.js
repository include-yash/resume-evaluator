import React, { useState } from "react";
import "./App.css";

function App() {
  const [inputResume, setInputResume] = useState(null);
  const [referenceResume, setReferenceResume] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const validateFile = (file) => {
    if (!file) return false;
    if (file.type !== "application/pdf") {
      setError("Only PDF files are supported.");
      return false;
    }
    if (file.size > 5 * 1024 * 1024) {
      setError("File size should be less than 5MB.");
      return false;
    }
    return true;
  };

  const handleFileChange = (e, setter) => {
    const file = e.target.files[0];
    if (validateFile(file)) {
      setter(file);
      setError("");
    } else {
      setter(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError("");

    if (!inputResume || !referenceResume) {
      setError("Both resumes are required.");
      return;
    }

    const formData = new FormData();
    formData.append("input_resume", inputResume);
    formData.append("reference_resume", referenceResume);

    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/api/v1/evaluate", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Resume evaluation failed.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "Unexpected error occurred.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">Resume Evaluator</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="input-resume">Candidate Resume (PDF)</label>
            <input
              id="input-resume"
              type="file"
              accept="application/pdf"
              onChange={(e) => handleFileChange(e, setInputResume)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="reference-resume">Reference Resume (PDF)</label>
            <input
              id="reference-resume"
              type="file"
              accept="application/pdf"
              onChange={(e) => handleFileChange(e, setReferenceResume)}
            />
          </div>
          {error && <div className="error">{error}</div>}
          <button type="submit" disabled={loading}>
            {loading ? "Evaluating..." : "Evaluate"}
          </button>
        </form>

        {result && (
          <div className="result-box">
            <h2>Evaluation Result</h2>
            <p>
              <strong>Score:</strong> {result.score}
            </p>
            <p>
              <strong>Reasoning:</strong> {result.reasoning}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
