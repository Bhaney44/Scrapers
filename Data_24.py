#Imported Libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, NavigableString, Tag
import csv

##Internet
#Link to webpage with patent
html = urlopen("Link")
#Soup object
soup = BeautifulSoup(html, 'html.parser')

##Scraper
#Get Data
def get_data():
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title = Title_Data[3].text.strip('\t\r\n')
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip()
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    #Return Variables
    return Patent_Number, Title, Assignee, Date
#Get Claims
def get_claims():
    for br in soup.findAll('br'):
        Claims = br.nextSibling
        if not (Claims and isinstance(Claims,NavigableString)):
            continue
        next2_s = Claims.nextSibling
        if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
            text = str(Claims).strip()
            if text:
                return Claims


#Write to Database
##Storage
def write():
    ##Get Variables
    Patent_Number, Title, Assignee, Date = get_data()
    Claims = get_claims()
    #Openfile
    with open('database.csv', 'a') as csvfile:
        #define fieldnames
        fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date', 'Claims']
        #Define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write
        writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date, 'Claims':Claims})

#Call function
write()




 
