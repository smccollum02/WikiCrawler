import requests
from bs4 import BeautifulSoup
baseUrl = "https://en.wikipedia.org"
depthLimit = 3

def crawler(startUrl):
    linksToVisit = [baseUrl + startUrl]
    depth = 0
    while depth < depthLimit and len(linksToVisit) > 0:
        for link in linksToVisit:
            response = requests.get(baseUrl + link)
            soup = BeautifulSoup(response.text, "html.parser")
            article = soup.find("div", id="bodyContent")
            aTags = soup.select("a")
            links = filter(lambda a: a != None and a.startswith("/wiki/"), [a.get("href") for a in aTags])


crawler("/wiki/Dubstep")