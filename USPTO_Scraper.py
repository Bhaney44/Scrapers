import sys
sys.path.append('/anaconda3/lib/python3.7/site-packages')

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://economics.nd.edu/faculty/rudiger-bachmann/")

bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
