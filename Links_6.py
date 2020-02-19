from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


#Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#pages
pages = set()

#getLinks function takes pageURL argument
def getLinks(pageURL):
    global pages

    ##Internet
    
    html = urlopen("LINK")
    #Soup object
    soup = BeautifulSoup(html, 'html.parser')

    try:
        print(soup.a.get_text())
    except AttributeError:
        print("This page is missing something.")

    for link in soup.find_all("a", href=re.compile('http')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #New Page
                newPage = link.attrs['href']
                print("-------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")






