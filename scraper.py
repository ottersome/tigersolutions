import requests
from bs4 import BeautifulSoup
import geograpy
import nltk

listOfWebsites = [\
        ]

class Scraper:
    def __init__(curLocation, symptoms):
        self.curLocation = curLocation
        self.symptoms = symptoms
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
    def getUnfilteredArticles(mainSource):
        for source in mainSources:
            pass

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())

