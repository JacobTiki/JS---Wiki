import wikipediaapi
import time

userAgent = "JS---Wiki (jacobososa08@gmail.com)"
wiki = wikipediaapi.Wikipedia(userAgent, "en")

def fetchLinks(page):
    linksList = []
    links = page.links

    for title in links.keys():
        linksList.append(title)

    return linksList

#creating start and target pages
startPage = wiki.page("Puerto Rico")
targetPage = wiki.page("Christianity")

print(fetchLinks(startPage))