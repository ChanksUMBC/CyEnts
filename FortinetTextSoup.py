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
    body = soup.find_all("div", "cmp cmp-text aem-GridColumn aem-GridColumn--default--12")

    for item in body:
        text = item.stripped_strings
        if text:
            for string in text:
                strings.append(string)

    #then i join them together by newline and i have some nice text to sift through
    joinChar = " "
    text = joinChar.join(strings)
    return text

def GetUnstrippedText(soup):

    strings = []

    body = soup.find_all("div", "cmp cmp-text aem-GridColumn aem-GridColumn--default--12")
    
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
    source = result.content
    soup = BeautifulSoup(source, "lxml")
    #print(soup.prettify())
    headers = soup.find_all("feedburner:origlink")

    linkList = []

    for header in headers:
        linkList.append(header.contents[0])
    
    return linkList
    

def Main():
    sourceList = ["http://feeds.feedburner.com/fortinet/blog/threat-research"]

    with open("fortinetText.jsonl","w",encoding="utf-8") as file:
        for source in sourceList:

            linkList = GetRSSLinkList(source)

            data = {"data": []}

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
                json.dump(source, file, ensure_ascii=False)
                file.write("\n")

                data["data"].append(source)

    with open("fortinetText.json","w",encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    with open("fortinetParagraphgs.txt", "w",encoding="utf-8") as file:
        for source in sourceList:

            linkList = GetRSSLinkList(source)

            for url in linkList:
                print(url)

                soup = GetSoup(url)

                text = GetUnstrippedText(soup)

                for item in text:
                    file.write(item)
                    file.write("\n")
                    file.write(":\/:")
                    file.write("\n")