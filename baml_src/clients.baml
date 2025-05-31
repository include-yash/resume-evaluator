client<llm> CustomGemini {
  provider google-ai
  options {
    model "gemini-2.0-flash"
    generationConfig {
      temperature 0
    }
    api_key env.GEMINI_API_KEY
  }
}

retry_policy Exponential {
  max_retries 2
  strategy {
    type exponential_backoff
    delay_ms 300
    multiplier 1.5
    max_delay_ms 10000
  }
}