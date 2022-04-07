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
    
    body = soup.find_all("div", "entry-content")

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
    result = requests.get(rssURL)
    source = str(result.content)

    listOfLinks = []

    splitSource = source.split("<item>")
    splitSource = splitSource[1:]

    for entry in splitSource:

        splitEntry = entry.split("<link>")
        firstLink = splitEntry[1].split("</link>")
        listOfLinks.append(firstLink[0])

    return listOfLinks


def Main():
    sourceList = ["https://blogs.juniper.net/threat-research/feed"]

    for source in sourceList:

        linkList = GetRSSLinkList(source)

        data = {"data": []}

    with open("juniperText.jsonl","w") as file:
        for url in linkList:
            print(url)

            soup = GetSoup(url)
            source = GetSource(url)

            currTime = GetCurrTime()

            text = GetText(soup)
            timeCreated = GetTimeCreated(soup)

            metadata = {"dateAccessed":currTime, "dateCreated":timeCreated, "source":source}
            info = {"metadata" : metadata, "text": text}
            source = {url: info}
            json.dump(source, file)

            data["data"].append(source)

    with open("juniperText.json","w") as file:
        json.dump(data, file, indent=4)
    