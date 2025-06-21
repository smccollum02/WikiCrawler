import json

articles = []
with open("storage.json", "r") as f:
    articles = json.load(f)
    for article in articles:
        classification = input("What should this article be classified as? " + article["link"])
        article["classification"] = classification

open('storage.json', 'w').close()
with open("storage.json", "w") as f:
    json.dump(articles, f, indent=4)