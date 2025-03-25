from config import *
import requests

clave = api_key

parametros = {

    "lat": latitud,
    "lon": longitud,
    "appid": api_key,
    "cnt": 4
}

respuesta = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parametros)
respuesta.raise_for_status()
data_weather = respuesta.json()

will_rain = False

for hour_data in data_weather["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")   
    
    
# print "bring an umbrella" if any of the weather condition codes is less than 700 in the next 12-hour window.