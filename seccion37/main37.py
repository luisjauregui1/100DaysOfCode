# Métodos avanzados de autenticación utilizando headers y peticiones POST, PUT y DELETE

import requests
import os
from datetime import datetime
from config import *

# Constantes
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph2"
GRAPH_NAME = "Grafica de curso"
GRAPH_UNIT = "leccion"
GRAPH_TYPE = "int"
GRAPH_COLOR = "sora"

# Fecha actual en formato requerido por Pixela
today = datetime.now().strftime("%Y%m%d")
hoy = datetime.now().strftime("%d-%b-%Y")
# Headers de autenticación
headers = {
    "X-USER-TOKEN": TOKEN
}

# --- Agregar un pixel a la gráfica ---
def agregar_pixel(cantidad):
    post_pixel_url = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    
    pixel_data = {
        "date": today,
        "quantity": str(cantidad)
    }

    try:
        response = requests.post(url=post_pixel_url, json=pixel_data, headers=headers)
        response.raise_for_status()
        print("\n✅ Registro exitoso:", response.text)
    
    except requests.exceptions.HTTPError as errh:
        print("❌ Error HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("❌ Error de conexión:", errc)
    except requests.exceptions.Timeout as errt:
        print("❌ Error de timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("❌ Error inesperado:", err)


# --- Menú principal ---
def main():
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("📊 Habit Tracker API")
        print("1. Registrar lecciones del día")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(f"\n📅 Registro para hoy: {hoy}")
            lecciones = input("¿Cuántas lecciones completaste? : ")
            if lecciones.isdigit():
                agregar_pixel(lecciones)
            else:
                print("⚠️ Por favor, ingresa un número válido.")
                
            input("\nPresiona ENTER para continuar...")

        elif opcion == "2":
            print("👋 ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida.")
            input("\nPresiona ENTER para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()