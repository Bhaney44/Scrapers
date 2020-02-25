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
    print(new_link)
    
get_link()

    
#Print Out
##United States Patent: 10530579
##/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=32&f=G&l=50&co1=AND&d=PTXT&s1=(%22deep+learning%22.CLTX.+or+%22deep+learning%22.DCTX.)&OS=ACLM/"deep+learning"



