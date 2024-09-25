from typing import List
import requests


API = "YOUR_OPENWEATHER_API_KEY"

def get_lat_lon(api: str, city: str) -> List[float]| List[None]:
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={api}'

    response = requests.get(url).json()

    if len(response) == 0:
        return [None, None]

    response = response[0]

    return [response['lat'], response['lon']]


def get_weather(city: str, api=API) -> dict | None:

    if "#" in city:
        return None

    lat, lon = get_lat_lon(api, city)

    if not lat:
        return

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric'

    response = requests.get(url).json()
    data = {'temp': response['main']['temp'],
            'feels_like' : response['main']['feels_like'],
            'sea_level' : response['main']['sea_level'],
            'speed_wind' : response['wind']['speed'],
            'country' : response['sys']['country']}

    return data

