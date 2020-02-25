#Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

##Internet
#Link to webpage 
web_page = urlopen("LINK")
#Soup object
soup = BeautifulSoup(web_page, 'html.parser')

##Get Data
def get_title():
    #Patent Number
    Patent_Number = soup.title.text
    print(Patent_Number)

get_title()


#Get
def get_link():
    ##Internet
    #Link to webpage 
    html = urlopen("LINK")
    #Soup object
    soup = BeautifulSoup(html, 'html.parser')
    #Find image
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    #Follow link
    ##link = image.parent
    link = image.parent
    new_link = link.attrs['href']
    #Insert initial part of link
    new_page = urlopen('"LINK"'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number = soup.title.text
    print(Patent_Number)
    
get_link()

    


