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

####
##I want to find a link on the page. This returns the correct link.
####

#Get
def get_link():
    ##Internet
    #Link to webpage 
    html = urlopen("LINK")
    #Soup object
    soup = BeautifulSoup(html, 'html.parser')
    #Find image
    ##image = <img valign="MIDDLE" src="/netaicon/PTO/nextdoc.gif" border="0" alt="[NEXT_DOC]">
    #image = soup.find("img", valign="MIDDLE")
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    #Follow link
    ##link = image.parent
    link = image.parent
    new_link = link.attrs['href']
    #new_url = 'http://patft.uspto.gov/'+new_link
    #new_page = urlopen(new_url)
    new_page = urlopen('http://patft.uspto.gov/'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number = soup.title.text
    print(Patent_Number)
    
get_link()

    
#Print Out
##United States Patent: 10530579
##

