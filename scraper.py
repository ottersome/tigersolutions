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
            res += str(self.scrapeTextForLocation(link))
            res += "\n"
        return res
    def scrapeTextForLocation(self,pageText):
        locations = {}
        doc = self.nlp_wk(pageText)
        locations = {ent.text for ent in doc.ents if ent.label_ in ['GPE']}
        for ent in doc.ents:
            if ent.label_ in ['GPE'] and ent.text not in locations:
                locations[ent.text]
        return locations
    def organizeList(self):
        #Organize score of list
        listWithScore = self.getScoredLists()
        listWithScore.sort(key=Scraper.sortByScore,reverse=True)
        return listWithScore

    @staticmethod
    def sortByScore(element):
        return element[1]
    # Python sorts in ascending mode by default
    # In this function we will score each url
    #   by the amount of matches it has for both location and symptom
    #
    def getScoredLists(self):
        scoredList = []
        for url in self.finalList:
            req =  Request(url,headers={'User-Agent': 'Mozilla/5.0'})
            pageText = Scraper.text_from_html(urlopen(req))

            #Geting Locations match
            locationsMatch = 0
            locations = self.scrapeTextForLocation(pageText)
            if len(locations) >0:
                for location in locations:
                    if location in self.curLocation:
                        locationsMatch += 1
                        continue
            symptomsMatch = 0
            for symptom in self.symptoms:
                if symptom in pageText:
                    symptomsMatch += 1
                    continue
            scoredList.append([url,symptomsMatch+locationsMatch])
        return scoredList

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

