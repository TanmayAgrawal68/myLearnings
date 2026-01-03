from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from src.providers.llmProvider import GeminiModelProvider
from src.providers.agentProvider import SpawnAgent
from dotenv import load_dotenv

import os
load_dotenv()
geminiModelProvider = GeminiModelProvider()
agentSpawner = SpawnAgent()
model = geminiModelProvider.get_model()
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = agentSpawner.get_agent(model=model, tools=[get_weather])

def main() :
    print("welcome to main file")
    response = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
    print(response)

if __name__ == "__main__":
    print("This is the main module being run")
    main()