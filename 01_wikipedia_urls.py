#Esto se está trabajando en un entorno virtual, para activar el entorno virual se usa el comando ".\scrapingEnv\Scripts\activate"

#El siguiente script lo que hace es buscar todas las etiquetas "a" que se encuentran en la url solicitada en la página.
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")

bsObj = BeautifulSoup(html, features="html5lib")

for link in bsObj.findAll("a"):
  #Se buscan todas las etiquetas "a" que existen en el objeto
  if "href" in link.attrs:
    #Se obtienen todos los "href" de los links que tengan "attrs href"
    print(link.attrs["href"])