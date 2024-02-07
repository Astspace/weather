class CantGetCoordinates(Exception):
    '''Программа не может получить координаты'''
    pass

class ApiSreviceError(Exception):
    '''Программа не может получить погоду'''
    pass

class WeatherFormatError(Exception):
    '''Программа не может преобразовать данные о погоде'''
    pass