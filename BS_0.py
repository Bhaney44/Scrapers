#Crawler

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html)

##Print links that reside within the div with the id set to bodyContent
##Print links that do not contain colons
##Print links that begin /wiki/

for link in soup.find("div", {"id":"bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
