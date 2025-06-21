import requests
import json
from bs4 import BeautifulSoup
baseUrl = "https://en.wikipedia.org"
depthLimit = 1
s = requests.Session()
s.headers.update({'User-Agent': 'MyCustomAgent/1.0'})

class Node:
    def __init__(self, link):
        self.children = []
        self.link = link
        self.paragraphs = []
    
    def getLinks(self):
        aTags = []
        for p in self.paragraphs:
            aTags = aTags + p.select("a")
        return filter(lambda a: a != None and a.startswith("/wiki/"), [a.get("href") for a in aTags])

    def getParagraphs(self):
        paragraphs = []
        for p in self.paragraphs:
            paragraphs.append(str().join([string.split("<")[0] for string in p.text.split(">")]))
        return paragraphs
    
    def toStorageJSON(self):
        return {
            "link": self.link,
            "paragraphs": self.getParagraphs()
        }


def crawl(startUrl):
    rootNode = Node(baseUrl + startUrl)
    nodesToVisit = [rootNode]
    depth = 0
    while depth < depthLimit and len(nodesToVisit) > 0:
        newNodes = []
        for node in nodesToVisit:
            response = s.get(node.link)
            soup = BeautifulSoup(response.text, "html.parser")
            node.paragraphs = soup.find("div", class_="mw-content-ltr").find_all("p")
            links = node.getLinks()
            node.children = [Node(baseUrl + link) for link in links]
            newNodes = newNodes + node.children
        nodesToVisit = newNodes
        depth += 1

    for node in nodesToVisit:
        response = s.get(node.link)
        soup = BeautifulSoup(response.text, "html.parser")
        node.paragraphs = soup.find("div", class_="mw-content-ltr").find_all("p")
    
    return getNodesListFromRoot(rootNode)

def getNodesListFromRoot(rootNode):
    nodes = [rootNode]
    children = rootNode.children
    while len(children) > 0:
        newChildren = []
        for node in children:
            nodes.append(node)
            newChildren = newChildren + node.children
        children = newChildren
    return nodes
        

nodes = crawl("/wiki/Dubstep")
nodesStorage = []
for node in nodes:
    nodesStorage.append(node.toStorageJSON())
open('storage.json', 'w').close()
with open("storage.json", "w") as f:
    json.dump(nodesStorage, f, indent=4)