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


def main():
    print("welcome to main file")
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "what is the weather outside? also tell me if you tell which is my location ?",
                }
            ]
        },
        config=config,
        context=Context(user_id="2"),
    )
    res = response["structured_response"]
    print(res)
    print("Punny Response:", res.punny_response)
    print("Weather Conditions:", res.weather_conditions)


if __name__ == "__main__":
    print("This is the main module being run")
    main()
