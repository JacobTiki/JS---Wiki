import wikipediaapi
import time
from queue import Queue

userAgent = "JS---Wiki (jacobososa08@gmail.com)"
wiki = wikipediaapi.Wikipedia(userAgent, "en")

def fetchLinks(page):
    linksList = []
    links = page.links

    for title in links.keys():
        linksList.append(title)

    return linksList

def wikipediaSolver(startPage, targetPage):
    print("Working on it...")
    startTime = time.time()

    visited = set()
    queue = Queue()
    parent = {}

    while not queue.empty():
        currentPageTitle = queue.get()
        if currentPageTitle == targetPage.title:
            break

        currentPage = wiki.page(currentPageTitle)
        links = fetchLinks(currentPage)

        for link in links:
            if(link not in visited):
                queue.put(link)
                visited.add(link)
                parent[link] = currentPageTitle

    path = []
    pageTitle = targetPage.title
    while pageTitle != startPage.title:
        path.append(pageTitle)
        pageTitle = parent[pageTitle]
    path.append(startPage.title)
    path.reverse()

    endTime = time.time
    print("This took", endTime - startTime, "seconds")
    return

#creating start and target pages
startPage = wiki.page("Puerto Rico")
targetPage = wiki.page("Barack Obama")
path = wikipediaSolver(startPage, targetPage)
print(fetchLinks(startPage))

