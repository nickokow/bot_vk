import requests
from requests import *
import json
from json import *
import urllib.request
s_city = ['Yekaterinburg (RU)']
city_id = 1486209
appid = "51e4d3328a1378ed9ddf332dd04644df"
def get_json():
    jurl = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid}).json()
    return jurl
def json_result():
    data = get_json()
    sity = str("В ")
    street = str("Сейчас на улице: ")
    temt = str("Температура сейчас: ")
    feels = str("Ошущается как: ")
    return  sity, data['name'], street, data['weather'][0]['description'], temt, data['main']['temp'], feels, data['main']['feels_like']
