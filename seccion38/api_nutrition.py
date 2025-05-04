from config import *
from datetime import datetime
import requests

now = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

input_user = input("Tell me whick exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/6847a69529e837956b44c4fd4592e024/ejercicioApi/hoja1"

headers = {
    "Content-Type": "application/json",
    "x-app-id": x_app_id,
    "x-app-key": x_app_key
}

data = {
    "query": input_user,
    "weight_kg": my_weight,
    "height_cm": my_height
}

# Api de ejercicio "Natural Language for Exercise"
response = requests.post(url=exercise_endpoint, json=data, headers=headers)
datos = response.json()
lendatos = len(datos["exercises"])


for i in range(lendatos):
    
    ejercicio = datos["exercises"][i]["name"] # exercise
    duracion = datos["exercises"][i]["duration_min"] # duration
    calorias = datos["exercises"][i]["nf_calories"] # calorias 
    
    new_row = {
        "hoja1": {
            "date": now,
            "time": current_time,
            # lo que esta en la respuesta de la api. tenemos que asignar valor y agregar
            "exercise": ejercicio,
            "duration": duracion,  # lo mismo para esto
            "calories": calorias  # y lo mismo buscar su valor en la api y asignar para enviar a hoja de calculo
        }
    }
    
    headers_sheety = {
        "Authorization": app_sheety_basic_key
    }
    

    response = requests.post(url=sheety_endpoint, json=new_row, headers=headers_sheety)
    respuesta = response.json()
    print(respuesta)