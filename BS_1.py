#Crawler

#Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

#Random see to navigate randomly
random.seed(datetime.datetime.now())

#getLinks function
#Takes an article url
#Retrieves article
def getLinks(articleURL):
    html = urlopen("https://en.wikipedia.org"+articleURL)
    soup = BeautifulSoup(html)
    return soup.find("div", {"id":"bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

