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
    max_temp_c_list = []
    min_temp_c_list = []
    cond_list = []
    cond_list_pic = []
    date_list = []

    feels_like = data_json['current']['feelslike_c']
    with open('res.json', 'w') as file:
        json.dump(data_json, file, indent=4)
    for i in range(days):
        date_list.append(data_json['forecast']['forecastday'][i]['date'])
        max_temp_c_list.append(
            data_json['forecast']['forecastday'][i]['day']['maxtemp_c'])
        cond_list.append(
            data_json['forecast']['forecastday'][i]['day']["condition"]['text'])
        cond_list_pic.append(
            data_json['forecast']['forecastday'][i]['day']["condition"]['icon'])
        min_temp_c_list.append(
            data_json['forecast']['forecastday'][i]['day']['mintemp_c'])
    print(cond_list_pic)
    return max_temp_c_list, cond_list, feels_like, cond_list_pic, min_temp_c_list, date_list


# get_weather(location='london', days=2)
