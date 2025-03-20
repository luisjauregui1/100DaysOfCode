import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

respuesta = requests.get("https://opentdb.com/api.php", params=parameters)
respuesta.raise_for_status()
datos = respuesta.json()
question_data = datos['results']