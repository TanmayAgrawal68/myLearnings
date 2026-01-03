# llm/provider.py
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class GeminiModelProvider:
    def __init__(
        self,
        model_name: str = "gemini-2.5-flash-lite",
        temperature: float = 1.0,
        max_tokens: int | None = None,
        timeout: int | None = None,
        max_retries: int = 2,
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries

    def get_model(self):
        return ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            timeout=self.timeout,
            max_retries=self.max_retries,
        )
