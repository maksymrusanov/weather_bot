import json
from dotenv import load_dotenv
from os import getenv
import requests
import pprint

load_dotenv()
API = getenv('API')
body = {'key': API,
        'q': 'london'}
request = requests.get(
    url='http://api.weatherapi.com/v1/current.json', params=body)
data_json = request.json()


with open('res.json', 'w') as file:
    json.dump(data_json, file, indent=4)


temp_c = data_json['current']['temp_c']
cond = data_json['current']['condition']['text']
feels_like = data_json['current']['feelslike_c']
print(temp_c)
print(cond)
print(feels_like)
