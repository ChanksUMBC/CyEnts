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
def GetTimeCreated(text):
    monthDict = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June" : "06", "July" : "07", "August" : "08", "September" : "09", "October": "10","November" : "11", "December" : "12" }

    titleAndTime = text.split("•")[0]
    time = titleAndTime.split(" ")[-4:]
    timeCreated = ""
    timeCreated += time[2] + "-"
    timeCreated += monthDict[time[0]] + "-"
    timeCreated += time[1][:-1].rjust(2,"0")

    return timeCreated


def GetText(soup):

    strings = []
    #this creates a list of human readable strings on the page
    
    body = soup.find_all("article")

    for item in body:
        text = item.stripped_strings
        i = 0
        if text:
            for string in text:
                strings.append(string)
                i+=1

    #then i join them together by newline and i have some nice text to sift through
    joinChar = " "
    text = joinChar.join(strings)
    return text


def GetUnstrippedText(soup):

    strings = []
    #this creates a list of human readable strings on the page
    
    body = soup.find_all("article")

    for item in body:
        text = item.strings
        for line in text:
            if(len(line) >= 100):
                strings.append(line)

    return strings


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

def getSourceList(json_past):

    source_list = []
    for source in json_past["data"]:
        for link in source:
            source_list.append(link)
    
    return source_list


def Main():
    sourceList = ["https://www.recordedfuture.com/category/cyber/feed/"]

    for source in sourceList:

        linkList = GetRSSLinkList(source)

        data = {"data": []}

    
    past_data = {}
    with open("CyberText/cyberJson/recordedFutureText.json", "r", encoding="utf-8") as file:
        past_data = json.load(file)
    
    source_list = getSourceList(past_data)
    data = past_data

    with open("CyberText/cyberJson/recordedFutureText.jsonl","w",encoding="utf-8") as file:
        for url in linkList:
            if(url not in source_list):
                print(url)

                soup = GetSoup(url)
                source = GetSource(url)

                currTime = GetCurrTime()

                text = GetText(soup)
                timeCreated = GetTimeCreated(text)

                metadata = {"dateAccessed":currTime, "dateCreated":timeCreated, "source":source}
                info = {"metadata" : metadata, "text": text}
                source = {url: info}
                json.dump(source, file, ensure_ascii=False)
                file.write("\n")

                data["data"].append(source)

    with open("CyberText/cyberJson/recordedFutureText.json","w",encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)