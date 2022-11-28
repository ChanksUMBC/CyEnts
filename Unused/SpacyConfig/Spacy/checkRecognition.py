import spacy
from spacy import displacy
import subprocess
import sys

modelName = "testModel"
wordVecs = "cyberWordVecWords.txt"

#IMPORTANT
#before running this code load the word vectors into the model with the command:
#python -m spacy init vectors en cyberWordVecWords.txt model


articles = []

with open("fireeyeText.jsonl", "r", encoding = "utf-8") as file:
    for line in file:
        articles.append(line.split("\"text\": \"")[1].replace("\"}}", ""))


nlp = spacy.load("en_core_web_lg")
doc = nlp(articles[0])


#this creates an html object that will display the senteces, different styles
#dep and ent, could also use the serv function, render saves the data
# dep creates a kind of sentence tree that shows the relation ships between words
#the other style option "ent" shows named entity recognition
#this will show what is being grabbed an why
# to customize this to only show one type of entity create a dictionary like
#options = {"ents" = ["Person"]} and pass that in as an options parameter
#like options=options into the render function
html = displacy.render(doc, style="ent")

#that line creates an html file so now we have to save it
with open("dataVis3.html", "w") as f:
    f.write(html)