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
def get_data():
    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip()
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    
    return Patent_Number, Title, Assignee, Date

get_data()

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
    new_page = urlopen('LINK'+new_link)
    soup = BeautifulSoup(new_page, 'html.parser')

#def next_page():
    #soup = get_link()
    #soup = BeautifulSoup(new_page, 'html.parser')

    #Patent Number
    Patent_Number = soup.title.text
    #Patent Title
    Title_Data = soup.find_all('font')
    Title_0 = Title_Data[3].text.strip('\t\r\n')
    Title = Title_0.strip()
    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignee = Assignee_Data[7].text.strip()
    #Date
    Date_Data = soup.find_all('b')
    Date_0 = Date_Data[3].text.strip('\t\r\n')
    Date = Date_0.strip()
    #Write to Database
    ##Storage
    def write():
        #Openfile
        with open('database.csv', 'a') as csvfile:
            #define fieldnames
            # 
            fieldnames = ['Patent_Number','Title', 'Assignee', 'Date']
            #Define writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #Write
            # 
            writer.writerow({'Patent_Number': Patent_Number,'Title':Title, 'Assignee':Assignee, 'Date':Date})
    #Call function
    write()
    
get_link()



