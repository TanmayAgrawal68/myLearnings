from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime


@tool
def get_weather_for_location(city: str) -> str:
    """Get weather information for a given city."""
    return f"The weather in {city} is sunny with a high of 75°F."


@dataclass
class Context:
    """Custom runtime context schema"""

    user_id: str


@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Get the user's location based on their user ID."""
    user_id = runtime.context.user_id
    # In a real implementation, you would look up the user's location from a database
    return "florida" if user_id == "1" else "SF"
