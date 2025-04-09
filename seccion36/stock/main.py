from config import *
import requests
from datetime import datetime, timedelta
import json
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Fecha de hoy
hoy = datetime.today()
hoy_formateado = hoy.strftime('%Y-%m-%d')

# mes para api de noticias!
hoy_menos_5 = hoy - timedelta(days=5)
mes_formateado = hoy_menos_5.strftime("%Y-%m-%d")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def calcular_porcentaje(valor_inicial, valor_final):
    return ((valor_final - valor_inicial) / valor_inicial) * 100

def alphavantage():
    parametros_alpha = {
        # https://www.alphavantage.co/query
        "function": "TIME_SERIES_DAILY",
        "symbol": "NVDA",
        "interval": "5min",
        "apikey": api_key_alpha
    }
    # llamada a la api de stock
    respuesta_alpha = requests.get("https://www.alphavantage.co/query", params=parametros_alpha)
    respuesta_alpha.raise_for_status()
    # respusta en formato json
    data_alpha = respuesta_alpha.json()
    # hacer lista de fechas 
    time_series = list(data_alpha["Time Series (Daily)"].keys())
    # ultimas 3 fechas disponibles 
    ult_reg = time_series[0]
    pen_reg = time_series[1]
    anti_reg = time_series[2]

    # obtener el valor en flotante del cierre correspondiente.
    ayer_reg_precio = float(data_alpha["Time Series (Daily)"][ult_reg]["4. close"])
    antier_reg_precio = float(data_alpha["Time Series (Daily)"][pen_reg]["4. close"])
    # calcaular el porcentaje de los cierres.
    crecimiento_dos_uno = calcular_porcentaje(antier_reg_precio,ayer_reg_precio)
    # condicion temporal!
    if crecimiento_dos_uno >= 5:
        print(f"NVDA: 🔺{crecimiento_dos_uno:.2f}%")
    elif crecimiento_dos_uno <=5:
        print(f"NVDA: 🔺{crecimiento_dos_uno:.2f}%")
    else:
        print(f"else = NVDA: 🔺{crecimiento_dos_uno:.2f}%")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def organizar_fechas(data):
    data["articles"].sort(key=lambda x: x["publishedAt"], reverse=True)
    return data
    

def newapi():
    """
    Función que obtiene noticias recientes sobre un tema específico utilizando la API de NewsAPI.

    Parámetros:
    - q (str): Término o palabra clave para buscar noticias (ej. "Apple").
    - from (str): Fecha de inicio para filtrar noticias (formato YYYY-MM-DD).
    - to (str): Fecha de fin para filtrar noticias (formato YYYY-MM-DD).
    - sortBy (str): Cómo ordenar los resultados. Ejemplo: 'popularity' o 'publishedAt'.
    - language (str): El idioma de las noticias a filtrar, ejemplo: 'en' para inglés, 'es' para español.
    """
    
    new_parametros = {
        "q": "nvidia",
        "sortBy":"popularity",
        "from": hoy_menos_5,
        "to" : hoy_formateado,
        "language": "en",
        "apiKey": newsapi_key
        
    }

    news_res = requests.get("https://newsapi.org/v2/everything", new_parametros)
    news_res.raise_for_status()
    datos_news = news_res.json()
    # solo los articualos
    articulos_sort = organizar_fechas(datos_news)
    
    with open("articulos.txt", "w") as file:
        json.dump(articulos_sort, file, indent=4)
    
    articulo_uno_title = articulos_sort['articles'][0]["title"]
    articulo_uno_description = articulos_sort['articles'][0]["description"]
    articulo_dos_title = articulos_sort['articles'][1]["title"]
    articulo_dos_description = articulos_sort['articles'][1]["description"]
    articulo_tres_title = articulos_sort['articles'][2]["title"]
    articulo_tres_description = articulos_sort['articles'][2]["description"]
    
    titulo_uno = html.unescape(articulo_uno_title)
    descripcion_uno = html.unescape(articulo_uno_description)
    titulo_dos = html.unescape(articulo_dos_title)
    descripcion_dos = html.unescape(articulo_dos_description)
    titulo_tres = html.unescape(articulo_tres_title)
    descripcion_tres = html.unescape(articulo_tres_description)
    
    noticias = f"""
    Ultimas noticias de NVIDIA:\n1.- -{titulo_uno}-
    {descripcion_uno}.\n
    2.- -{titulo_dos}- 
    {descripcion_dos}.\n
    3.- -{titulo_tres}- 
    {descripcion_tres}
    """
    
    print(noticias)
        
        
newapi()




# print("Json guardado correctamente en data.txt")
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

