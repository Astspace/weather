from coordinates import Coordinates
import config
import urllib.request
from urllib.error import URLError
from exceptions import ApiSreviceError
import json
from json.decoder import JSONDecodeError
from enum import Enum
from datetime import datetime
from typing import Literal, TypeAlias
from dataclasses import dataclass
import pprint

Celcius: TypeAlias = float
MeterInSec: TypeAlias = float | str

class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    ATMOSPHERE = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celcius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str
    wind_speed: MeterInSec
    wind_speed_gust: MeterInSec

def get_weather(coordindates: Coordinates) -> Weather:
    openweather_dict = _get_openweather_responce(coordindates)
    weather = _parse_weather(openweather_dict)
    return weather

def _get_openweather_responce(coordinates: Coordinates) -> dict:
    url = config.OPENWEATHER_URL.format(
        latitude=coordinates.latitude,
        longitude=coordinates.longitude)
    try:
        openweather_response = urllib.request.urlopen(url).read()
    except URLError:
        raise ApiSreviceError("Не удалось получить данные о погоде")
    return _convert_openweather_dict(openweather_response)

def _convert_openweather_dict(openweather_response: bytes) -> dict:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiSreviceError("Не удалось обработать данные о погоде")
    return openweather_dict

def _parse_weather(openweather_dict: dict) -> Weather:
    temperature = _parse_temperature(openweather_dict)
    weather_type = _parse_weather_type(openweather_dict)
    sunrise = _parse_sun_time(openweather_dict, "sunrise")
    sunset = _parse_sun_time(openweather_dict, "sunset")
    city = _parse_city(openweather_dict)
    wind_speed = _parse_wind_speed(openweather_dict, "speed")
    if openweather_dict["wind"].get("gust", 0) != 0:
        wind_speed_gust = str(_parse_wind_speed(openweather_dict, "gust")) + " м/с"
    else:
        wind_speed_gust = "Не определена"
    return Weather(
        temperature=temperature,
        weather_type=weather_type,
        sunrise=sunrise,
        sunset=sunset,
        city=city,
        wind_speed=wind_speed,
        wind_speed_gust=wind_speed_gust
    )

def _parse_temperature(openweather_dict: dict) -> Celcius:
    try:
        temperature = round(openweather_dict["main"]["temp"])
    except Exception:
        raise ApiSreviceError("Не удалось вычислить температуру")
    return temperature

def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except Exception:
        raise ApiSreviceError("Не удалось вычислить тип погоды")
    weather_types = {
        "2": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.ATMOSPHERE,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiSreviceError("Не удалось определить тип погоды из числа имеющихся")

def _parse_sun_time(
        openweather_dict: dict,
        type_suntime: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    try:
        return datetime.fromtimestamp(openweather_dict["sys"][type_suntime])
    except Exception:
        raise ApiSreviceError("Не удалось определить время захода/восхода солнца")

def _parse_city(openweather_dict: dict) -> str:
    try:
        return openweather_dict["name"]
    except Exception:
        raise ApiSreviceError("Не удалось определить город")

def _parse_wind_speed(
    openweather_dict: dict,
    type_speed: Literal["speed"] | Literal["gust"]) -> MeterInSec:
    try:
        return openweather_dict["wind"][type_speed]
    except Exception:
        raise ApiSreviceError("Не удалось определить скорость ветра")


if __name__ == "__main__":
    pprint.pprint(get_weather(Coordinates(latitude=64.6, longitude=39.8)))