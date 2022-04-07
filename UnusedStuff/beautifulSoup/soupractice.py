import requests
from bs4 import BeautifulSoup

result = requests.get("https://edhrec.com/articles/ranking-every-equipment-with-edhrec-part-11-mr-steal-your-graveyard/")

#print(result.status_code)
#print(result.headers)

#this is just a bunch of garbage
#beautiful soup can make something of it
source = result.content
#print(source)

#make a soup object
#you kinda just need to have the lxml there its just a given
soup = BeautifulSoup(source, "lxml")
#print(soup.prettify())

urls = []

stuff = soup.find_all("p")

for thing in stuff:
    print(thing)

#<div class="Card_name__1MYwa">Profane Tutor</div>