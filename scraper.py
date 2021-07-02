#import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from bs4.element import Comment
#import geograpy
#import geopy
import spacy 
import nltk


class Scraper:
    def __init__(self,curLocation, symptoms,parentWebsites):
        self.curLocation = curLocation
        self.symptoms = symptoms
        #self.nlp_wk = spacy.load('xx_ent_wiki_sm')
        self.nlp_wk = spacy.load('en_core_web_sm')
        #nltk.download('punkt')
        #nltk.download('averaged_perceptron_tagger')
        #nltk.download('maxent_ne_chunker')
        #nltk.download('words')
        self.finalList  = self.getFinalLinks(parentWebsites)
    def __str__(self):
        res = ""
        for link in self.finalLinks:
            res += link+"\n\tLocation : "
            res += str(self.scrapeLinkForLocations(link))
            res += "\n"
        return res
    def scrapeLinkForLocations(self,url):
        locations = {}
        req =  Request(url,headers={'User-Agent': 'Mozilla/5.0'})
        page = Scraper.text_from_html(urlopen(req))
        doc = self.nlp_wk(page)
        locations = {ent.text for ent in doc.ents if ent.label_ in ['GPE']}
        for ent in doc.ents:
            if ent.label_ in ['GPE'] and ent.text not in locations:
                locations[ent.text]
        return locations
    def organizeList(self):
        #Organize First by a Location
            self.finalLinks.sort(key=self.sortPerLocations)
        #Organize Second by Symptoms
            self.finalLinks.sort(key=self.sortPerSymptoms)
    # Python sorts in ascending mode by default
    @staticmethod
    def sortPerLocations():
        #self.scrapeLinkForLocations(link).regions
        #TODO fxi this
        return len(interection(self.curLocation,self.curLocation))
        pass
    @staticmethod
    def sortPerSymptoms():
        pass
    @staticmethod
    def getFinalLinks(parentSources):
        finalSource = []
        for source in parentSources:
            if source == "http://www.sciencedaily.com/news/health_medicine/infectious_diseases/":
                req =  Request(source,headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req).read()
                soup = BeautifulSoup(page,"html.parser")
                results = soup.find(id="summaries")
                for link in results.find_all("a"):
                    finalSource.append("http://www.sciencedaily.com" + link['href'])
        return finalSource

    @staticmethod
    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.find(id='story_text')
        texts = soup.find(id='text')
        texts = texts.findAll(text=True)
        visible_texts = filter(Scraper.tag_visibleText, texts)  
        return u" ".join(t.strip() for t in visible_texts)
    @staticmethod
    def tag_visibleText(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

parentWebsites = [\
        "http://www.sciencedaily.com/news/health_medicine/infectious_diseases/",
        ]
scrappy = Scraper(None,None,parentWebsites)

print(scrappy)
