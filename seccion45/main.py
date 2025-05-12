from bs4 import BeautifulSoup
import lxml
import requests
import html

""""
with open('website.html') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")

print(soup.title) # imprime el titulo con toda la etiqueta
# ejeplo de repsueta: <title>Angela's Personal Site</title>
print(soup.title.name ) # imprime el nombre de la etiqueta
# Ejemplo de respuesta: title
print(soup.title.string) # imprime el contoendo de la etiqueta 
# Ejemplo de respueta: Angela's Personal Site

print(soup.prettify()) # ESTO ES Para que se idente el contendio de html


all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags) # Imprimie una lista con todas las etiquetas a completa, ejemplo de respueta: [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]




all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText()) # Imprime el conenido, 
    # Ejemplo: The App Brewery
    # My Hobbies
    # Contact Me
    
    print(tag.get('href')) # retorna el link contendo de href ejemplo:
    # https://angelabauer.github.io/cv/hobbies.html
    

    
heading = soup.find(name="h1", id="name")
print(heading) # Imprime la primera etiqueta con los parametros encontrados



section_heading = soup.find(name="h3", class_="heading")
print(section_heading) # lo mismo que la anterior, imprime los valores imprime la primera etiqueta con los valore a buscar


company_url = soup.select_one(selector="p a")
print(company_url) # selecciona la primera y solo una de las etiqutas y retorna el conteidno completo ejemplo: <a href="https://www.paginaejemplo.com">nuevo contenido</a>



name = soup.select_one(selector="#name")
print(name) # seleciona el primero y solo uno. respuetas la etiqueta con el contenido: <h1 id="name">Valor Nuevo</h1>


heading = soup.select(selector=".heading")
print(heading) # retorna una lista con los valores de la clase heading.
# Ejemplo de respuesta: [<h3 class="heading">h3 Nuevo</h3>, <h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>] 👁️



form_tag = soup.find("input")
max_l = form_tag.get('maxlength')
print(max_l) # guardamos en una variable el contendo de el valor de maxlength que es un atributo de la etiquta <input> 

"""

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

print("--------mayor votos----------")
mas_alto = article_upvotes.index(max(article_upvotes))
print(article_texts[mas_alto])
print(article_links[mas_alto])
print(article_upvotes[mas_alto])

# titulos = soup.find_all(name="a", class_="storylink")
# article_upvotes = soup.find_all(name="span", class_="score")

# print(titulos.getText())
# print(titulos.get("href"))
# print(article_upvotes.getText())