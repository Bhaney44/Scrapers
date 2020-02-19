#Imported Libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv

##Internet
#Link to webpage with patent
html = urlopen("Link")
#Soup object
soup = BeautifulSoup(html, 'html.parser')

##Get Data
def get_data():
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    ##Title = Title_Data[3].text
    Title = Title_Data[3].text.strip('\t\r\n')
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip()
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    
    return Patent_Number, Title, Assignee, Date

#Write to Database
##Storage
def write():
    #Get variables
    Patent_Number, Title, Assignee, Date = get_data()
    #Openfile
    with open('database.csv', 'a') as csvfile:
        #define fieldnames
        fieldnames = ['Patent_Number', 'Title', 'Assignee', 'Date']
        #Define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write
        writer.writerow({'Patent_Number': Patent_Number, 'Title':Title, 'Assignee':Assignee, 'Date':Date})

#Call function
write()



