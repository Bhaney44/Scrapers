#WikiScrape

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Deep_learning")

soup = BeautifulSoup(html, features="lxml")

#Title
title = soup.find(id="firstHeading")

#Body
main_body = soup.findAll('p')
main_body = soup.p.prettify()



#print(main_body)

csvfile = open('wiki.csv', 'a')
writer = csv.writer(csvfile)
data_0 = (title)
data_1 = (main_body)
writer.writerow(data_0)
writer.writerow(data_1)

#body
    #content
        #div id = mw-content-text
            #div class = mw-content-text
                #<p><p>
                






