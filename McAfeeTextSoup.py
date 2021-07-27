import requests
import time
import json
from bs4 import BeautifulSoup

#this will return the current time in the format "year-month-day"
def GetCurrTime():
    currTime = ""
    timeObject = time.localtime()
    currTime += str(timeObject.tm_year)
    currTime += "-"
    currTime += str(timeObject.tm_mon).rjust(2,"0")
    currTime += "-"
    currTime += str(timeObject.tm_mday).rjust(2,"0")
    return currTime


#this will generate a BS object from a link
def GetSoup(link):

    result = requests.get(link)
    source = result.content
    soup = BeautifulSoup(source,"lxml")
    return soup


#this will get the time that the page was created
def GetTimeCreated(soup):
    meta = soup.find_all("meta",property="article:published_time")
    date = meta[0]["content"][:10]
    return date


def GetText(soup):

    strings = []
    #this creates a list of human readable strings on the page
    body = soup.find_all("div", "wrap-section padding-small article")

    for item in body:
        text = item.stripped_strings
        if text:
            for string in text:
                strings.append(string)

    #then i join them together by newline and i have some nice text to sift through
    joinChar = " "
    text = joinChar.join(strings)
    return text


def GetSource(url):

    splitURL = url.split("/")
    source = splitURL[2]
    return source


def GetRSSLinkList(rssURL):
    soup = GetSoup(rssURL)
    items = soup.find_all("item")

    listOfLinks = []
    for item in items:
        listOfLinks.append(item.contents[4].strip())

    return listOfLinks


def Main():
    sourceList = ["https://www.mcafee.com/blogs/tag/advanced-threat-research/feed"]

    for source in sourceList:

        linkList = GetRSSLinkList(source)

        data = {"data": []}

    with open("mcAfeeText.jsonl","w") as file:
        for url in linkList:
            print(url)


            soup = GetSoup(url)
            source = GetSource(url)

            currTime = GetCurrTime()

            timeCreated = GetTimeCreated(soup)
            text = GetText(soup)

            metadata = {"dateAccessed":currTime, "dateCreated":timeCreated, "source":source}
            info = {"metadata" : metadata, "text": text}
            source = {url: info}
            json.dump(source, file)
            file.write("\n")

            data["data"].append(source)

    with open("mcAfeeText.json","w") as file:
        json.dump(data, file, indent=4)