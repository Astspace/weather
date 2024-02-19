from weather_api_service import Weather
from exceptions import WeatherFormatError
from datetime import datetime


def format_weather(weather: Weather) -> str:
    try:
        return (f"\nДАННЫЕ О ПОГОДЕ:\n"
                f"Город - {weather.city}\n"
            f"Температура: {weather.temperature} °C\n"
            f"Скорость ветра: {weather.wind_speed} м/с\n"
            f"Скорость порывов ветра: {weather.wind_speed_gust}\n"
            f"Восход солнца: {weather.sunrise.strftime('%H:%M')}\n"
            f"Заход солнца: {weather.sunset.strftime('%H:%M')}\n"
            f"Время запроса: {datetime.now()}\n"
                )
    except Exception:
        raise WeatherFormatError("Невозможно преобразовать данные о погоде")


if __name__ == "__main__":
    '''test'''
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2024-07-22 07:00:00"),
        sunset=datetime.fromisoformat(("2024-07-22 16:00:00")),
        city="Северодвинск",
        wind_speed=1.07,
        wind_speed_gust=1.23
        )))