import requests
import json


def kelvin_to_celcius(kelvin):
    return kelvin - 273.15


api_key = "6d1875795bd8e165da0365137230fcf1"
adress = "http://api.openweathermap.org/data/2.5/weather?q="
city = input("Write a city (eg. London): ")

response = requests.get(adress + city + "&appid=" + api_key)
print("")


weather = response.json()["weather"][0]["description"]
celcius = round(kelvin_to_celcius(response.json()["main"]["temp"]))
feels_like = round(kelvin_to_celcius(response.json()["main"]["feels_like"]))
humidity = round(response.json()["main"]["humidity"])
wind = round(response.json()["wind"]["speed"])



print(f"""Its {celcius} degrees celcius
It feels like {feels_like} degrees celcius
Humidity is {humidity} %
The current wind speed is {wind} m/s
The current weather is: {weather}""")