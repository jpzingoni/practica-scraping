from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now().timestamp())

def getLinks(articleUrl):
  html = urlopen(f"http://en.wikipedia.org{articleUrl}")
  bsOjb = BeautifulSoup(html, features="html5lib")
  links = bsOjb.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
  return links

linky = getLinks("/wiki/Kevin_Bacon")

while len(linky) > 0:
  newArticle = linky[random.randint(0, len(linky)-1)].attrs['href']
  print(newArticle)
  linky = getLinks(newArticle)