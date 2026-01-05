from dataclasses import dataclass


@dataclass
class WeatherResponseFormat:
    """Response format for the weather agent."""

    # A punny response about the weather (Always required)
    punny_response: str
    # Any interesting information about the weather if Available
    weather_conditions: str | None = None
