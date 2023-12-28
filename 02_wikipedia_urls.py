#Esto se está trabajando en un entorno virtual, para activar el entorno virual se usa el comando ".\scrapingEnv\Scripts\activate"

#El siguiente script obtiene el div con el id "id: bodyContent" para luego buscar dentro de ese div todas las etiquetas "a" que matcheen con el patron a compilar en la expresión regular
from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsobj = BeautifulSoup(html, features="html5lib")
enlaces_validos = []
for link in bsobj.find("div", {"id":"bodyContent"}).findAll("a", href= re.compile("^(/wiki/)(.)*$")):
  if 'href' in link.attrs:
    print(unquote(link.attrs['href']))