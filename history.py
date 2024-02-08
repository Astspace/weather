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
        with open(self._file, "a") as f:
            f.write(f"Время запроса погоды: {now}\n"
                    f"{formatted_weather}\n")

def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    storage.save(weather)

class JSONFileWeatherStorage:
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile

    def save(self, weather: Weather) -> None:
        with open(self._jsonfile, "r") as f:
