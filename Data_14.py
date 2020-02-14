#Imported Libraries

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


#Write to Database
def write():
    #Link to webpage with patent
    html = urlopen("LINK")

    #Soup object
    soup = BeautifulSoup(html, 'html.parser')
    #Data
    #Patent Number
    Patent_Numbers = soup.title.text

    #Patent Title
    Title_Data = soup.find_all('font')
    Titles = Title_Data[3].text

    #Date
    Date_Data = soup.find_all('b')
    Dates = Date_Data[3].text

    #Inventor
    Inventor_Data = soup.find_all('b')
    Inventors = Inventor_Data[2].text

    #Assignee
    Assignee_Data = soup.find_all('b')
    Assignees = Assignee_Data[7].text

    #Claim
    #Claim =

    #Abstract
    Abstract_Data = soup.find_all('p')
    Abstracts = Abstract_Data[0].text
    
    #Openfile
    with open('database.csv', 'a') as csvfile:
    #define fieldnames
        #'Claims',
        fieldnames = ['Patent Number', 'Title', 'Date', 'Inventor', 'Assignee', 'Abstract']
    #define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #Write
        #'Claim':Claims,
        writer.writerow({'Patent Number': Patent_Numbers, 'Title':Titles, 'Date':Dates, 'Inventor':Inventors, 'Assignee': Assignees, 'Abstract':Abstracts})

#Call function
write()
 
