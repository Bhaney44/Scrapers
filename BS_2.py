#Crawler

#Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#pages
pages = set()

def getLinks(pageURL):
    global pages
    html = urlopen("https://en.wikipedia.org"+pageURL)
    soup = BeautifulSoup(html)
    for link in soup.find_all("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #New page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")




