from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.encoding = "uft-8"

soup = BeautifulSoup(response.text, "html.parser")

# recupere toda la pagina en una archvio para ver los valores a capturar
# soup_limpio = html.unescape(soup)
# with open("movie.html", "w", encoding="utf-8") as archivo:
#     archivo.write(str(soup_limpio))

# ejemplo: article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# capturar los titulos: con una lista de compresion:
all_movies = soup.find_all(name="h3", class_="title")

titulos_peliculas = [movie.getText() for movie in all_movies]
titulos_invetidos = titulos_peliculas[::-1]

with open("100movies.txt", mode="w", encoding="utf-8") as archivo:
    for nombre in titulos_invetidos:
        archivo.write(f"{nombre}\n")
