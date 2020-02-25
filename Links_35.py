#Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

def get_data():
    #page 0
    html = urlopen("LINK")
    soup = BeautifulSoup(html, 'html.parser')
    #Patent Number
    Patent_Number_0 = soup.title.text
    print(Patent_Number_0)
    
    #page 1
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number_1 = soup.title.text
    print(Patent_Number_1)
    
    #page 2
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number 
    Patent_Number_2 = soup.title.text
    print(Patent_Number_2)
    
    #page 3
    image = soup.find("img", valign="MIDDLE", alt="[NEXT_DOC]")
    link = image.parent
    new_link = link.attrs['href']
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')
    #Patent Number
    Patent_Number_3 = soup.title.text
    print(Patent_Number_3)

get_data()
    




