import requests
from bs4 import BeautifulSoup

listOfWebsites = [\
        'ZZ',\
        ]

class Scraper:
    def __init__(curLocation, symptoms):
        self.curLocation = curLocation
        self.symptoms = symptoms
    def 

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())

