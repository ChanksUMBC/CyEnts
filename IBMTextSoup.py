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
    monthDict = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June" : "06", "July" : "07", "August" : "08", "September" : "09", "October": "10","November" : "11", "December" : "12" }

    time = str(soup.find("div", "single__date-and-time").contents[0]).split(" ")
    timeCreated = ""
    timeCreated += time[2] + "-"
    timeCreated += monthDict[time[0]] + "-"
    timeCreated += time[1][:-1].rjust(2,"0")

    return timeCreated


def GetText(soup):

    strings = []
    #this creates a list of human readable strings on the page
    body = soup.find_all("div", "single__content-itself")

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
    titles = soup.find_all("h3", "article__title")
    titles = titles[:-1]

    linkList = []
    for link in titles:
        fullLink = link.find("a")
        linkList.append(fullLink.attrs["href"])

    return linkList


def Main():
    sourceList = ["https://securityintelligence.com/category/x-force/"]

    for source in sourceList:

        linkList = GetRSSLinkList(source)

        data = {"data": []}

    with open("ibmText.jsonl","w") as file:
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

    with open("ibmText.json","w") as file:
        json.dump(data, file, indent=4)