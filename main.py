import json
from dotenv import load_dotenv
from os import getenv
import requests
load_dotenv()
WEATHER_API = getenv('WEATHER_API')


def get_weather(location, days):
    body = {'key': WEATHER_API,
            'q': location,
            'days': days}
    request = requests.get(
        url='http://api.weatherapi.com/v1/current.json', params=body)
    data_json = request.json()

    # with open('res.json', 'w') as file:
    #     json.dump(data_json, file, indent=4)

    temp_c = data_json['current']['temp_c']
    cond = data_json['current']['condition']['text']
    feels_like = data_json['current']['feelslike_c']
    print(temp_c)
    print(cond)
    print(feels_like)
