#Get addresses
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
def getAddresses(pageURL):
    global pages
    ##Internet
    html = urlopen("LINK")
    #Soup object
    soup = BeautifulSoup(html, 'html.parser')


html = urlopen("https://algoscan.app/address/6G5V4U2MCW5TIZ7JP6BZFQELTGGJBEG5EVSQRQQRLEZM3V6DXOPV5TUJQA")
#Soup object
soup = BeautifulSoup(html, 'html.parser')
for i in soup.find_all('td'):
    addresses0 = soup.find_all('td')
    addresses1 = soup.find_all('a')
    #print(addresses0.string)
    #print('-----------')
    #print(addresses1.string)
##print(soup.prettify())

#soup_text = soup.get_text()
#print(soup_text)

#soupl.find_all('a')

addresses0 = soup.find_all('td')
#addresses1 = soup.find_all('a')
addresses2 = soup.find_all('href')
#print(addresses0)
print('-----------')
#print(addresses1)
#print(addresses2)
#addresses1 = soup.a
#addresses3 = addresses1.contents
#print(addresses3)
addresses1 = soup.find_all('td','a')

print(addresses1)
