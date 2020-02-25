from urllib.request import urlopen
from bs4 import BeautifulSoup


#Imported Libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv

##Internet
#Link to webpage with patent
html = urlopen("LINK")
#Soup object
soup = BeautifulSoup(html, 'html.parser')

def get_links():
    for link in soup.find_all('a'):
        links = link.get('href')
        with open('database.csv', 'a') as csvfile:
            fieldnames = ['Links']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            writer.writerow({'Links': links})

get_links()









