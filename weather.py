# coding: UTF-8
import requests
import json

import config

url = "https://community-open-weather-map.p.rapidapi.com/weather?q=Sapporo&lang=ja&units=metric"

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': config.RAPID_API_KEY
    }


def getInfo(num):
    response = requests.request("GET", url, headers=headers)
    res = {}
    res = json.loads(response.text)
    return res