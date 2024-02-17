from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, ApiSreviceError
from history import save_weather, TxtFileWeatherStorage
from pathlib import Path


def main():
    try:
        coordinates = get_gps_coordinates()
    except CantGetCoordinates:
        print("Не удалось получить GPS-координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiSreviceError:
        print(f"Не удалось получить погоду по координатам {coordinates}")
        exit(1)

    save_weather(weather,
                 TxtFileWeatherStorage(Path.cwd() / 'history.txt')
                 )

    return format_weather(weather)

if __name__ == "__main__":
    print(main())