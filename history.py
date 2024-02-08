from typing import Protocol
from weather_api_service import Weather
from pathlib import Path
from datetime import datetime
from weather_formatter import format_weather


class WeatherStorage(Protocol):
    def save(self, weather: Weather) -> None:
        raise NotImplementedError

class TxtFileWeatherStorage:
    def __int__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
