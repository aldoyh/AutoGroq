#APIs
LLM_PROVIDER = "groq" # Supported values: "groq", "openai"

GROQ_API_KEY_NAME = "GROQ_API_KEY"
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

OPENAI_API_KEY_NAME = "OPENAI_API_KEY"
OPENAI_API_KEY = "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"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 2  # in seconds
RETRY_TOKEN_LIMIT = 5000
LLM_URL = GROQ_API_URL

# Model configurations
MODEL_TOKEN_LIMITS = {
    'llama3-70b-8192': 8192,
    'llama3-8b-8192': 8192,
    'mixtral-8x7b-32768': 32768,
    'gemma-7b-it': 8192,
    'gpt-4o': 4096,
}