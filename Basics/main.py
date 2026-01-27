from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from src.providers.llmProvider import GeminiModelProvider
from src.providers.agentProvider import SpawnAgent
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy
from src.tools.weatherTool import get_weather_for_location, get_user_location, Context
from src.response_formatter.weather_res_format import WeatherResponseFormat
from src.prompts.weather_system_prompt import SYSTEM_PROMPT
import gradio as gr


load_dotenv()
geminiModelProvider = GeminiModelProvider()
agentSpawner = SpawnAgent()
model = geminiModelProvider.get_model()

# memmory initializer
checkpointer = InMemorySaver()

agent = agentSpawner.get_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(WeatherResponseFormat),
    checkpointer=checkpointer,
)
config = {"configurable": {"thread_id": "1"}}

def agentCall(message: str, history: list):
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message,
                }
            ]
        },
        config=config,
        context=Context(user_id="2"),
    )    
    res = response["structured_response"]
    return res.punny_response
def main():
    print("welcome to main file")

    demo = gr.ChatInterface(
    fn=agentCall,
    title="Weather Agent with Gemini Pro",
    description="Ask about the weather in different locations!",
    examples=[
            "What's the weather in Bangalore?",
            "Will it rain tomorrow?",
            "What about the place I asked earlier?"
        ]
    )

    demo.launch()



if __name__ == "__main__":
    print("This is the main module being run")
    main()
