import requests
from pprint import pprint

def get_weather_by_city_name(city_name):
    parameters = {
        'appid': '987f60f006e8f54c84589f6ed20de29b',
        'units': 'metric',
        'lang': 'ru',
        'q': city_name
    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', parameters)
    data = response.json()

    try:
        message = f""" В городе <b>{data['name']}</b>:
<i>{data['weather'][0]['description']}</i>,
Температура воздуха: {data['main']['temp']} градусов Цельсию    
"""
    except KeyError:
        message = 'Такого города не существует'

    return message
