from dataclasses import dataclass
import config
import json
from urllib.request import urlopen
from typing import TypedDict
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

class Datasite(TypedDict):
    ip: str
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str
    timezone: str
    readme: str


def get_gps_coordinates() -> Coordinates:
    coordinates = _get_coordinates_site()
    return _round_coordinates(coordinates)

def _get_coordinates_site():
    data_site = _get_data_site()
    coordinates = _parse_coordinates(data_site)
    return coordinates

def _get_data_site() -> Datasite:
    try:
        load_site = urlopen(config.DATA_URL)
    except Exception:
        print("Невозможно открыть URL")
        exit(1)
    data_site = json.load(load_site)
    return data_site

def _parse_coordinates(data_site: Datasite) -> Coordinates:
    try:
        coordinates_output = data_site['loc']
    except Exception:
        print("Не удалось вычислить координаты из полученных данных")
        exit(1)
    return _coord_list(coordinates_output)

def _coord_list(coordinates_output: str) -> Coordinates:
    try:
        coordinates_list = coordinates_output.split(",")
    except Exception:
        print("Не удалось распаковать полученные координаты")
        exit(1)
    if len(coordinates_list) != 2:
        raise CantGetCoordinates("Некорректно получены координаты")
    return _format_coordinates(coordinates_list)

def _format_coordinates(coordinates_list: list[str]) -> Coordinates:
    coordinates = Coordinates(
        latitude=float(coordinates_list[0]),
        longitude=float(coordinates_list[1])
    )
    return coordinates

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.ROUND_COORD:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())