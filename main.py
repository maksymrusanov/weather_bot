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
        url='http://api.weatherapi.com/v1/forecast.json', params=body)
    data_json = request.json()
    temp_c_list = []
    cond_list = []
    feels_like_list = []
    with open('res.json', 'w') as file:
        json.dump(data_json, file, indent=4)
    for i in data_json['forecast']['forecastday']:
        print(data_json['forecast']['forecastday'])

        # temp_c = data_json['current']['temp_c']
        # cond = data_json['current']['condition']['text']
        # feels_like = data_json['current']['feelslike_c']
        # return temp_c, cond, feels_like
        # print(temp_c_list)
        # print(cond_list)
        # print(feels_like_list)


get_weather(location='london', days=5)
