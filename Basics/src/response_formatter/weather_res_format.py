from dataclasses import dataclass


@dataclass
class WeatherResponseFormat:
    """Response format for the weather agent."""

    # A punny response about the weather and other questions (Always required)
    punny_response: str
    # Any interesting information about the weather if Available
    weather_conditions: str | None = None
    # Conversational response example telling if this question was asked before or not
    conversational_response: str | None = None
