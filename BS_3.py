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

    try:
        print(soup.h1.get_text())
        print(soup.find(id ="mw-content-text").find_all("p")[0])
        print(soup.find(id ="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something.")

    for link in soup.find_all("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #New Page
                newPage = link.attrs['href']
                print("-------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")


