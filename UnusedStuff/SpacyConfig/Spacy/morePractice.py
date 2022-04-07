import spacy
import textacy
from spacy import displacy

with open("./UMBCREU/Spacy/alice.txt", "r", encoding="utf8") as alice:
    #read the text and clean up all the line breaks and double line breaks
    text = alice.read().replace("\n\n", " ").replace("\n", " ")

    #split text up into chapters so it's easier to handle
    chapters = text.split("CHAPTER ")[1:]

#loads the pretrained model that spacy provides. there is also large which is more accurate
nlp = spacy.load("en_core_web_lg")

#loads in the first chapter into the nlp
doc = nlp(chapters[0])

#separates the text into sentences
sentences = list(doc.sents)
#print(sentences[1])

#searches for named entities
#ents is actually a tuple
entities = list(doc.ents)

"""
#numerical value
print(entities[0].label)
#this identifies Alice as a person! this is the type of entity that "alice" is
print(entities[0].label_)
#this is the text of the entity
print(entities[0].text)
"""

"""
#this will separate out all of the people in the text
people = []

for ent in entities:
    if ent.label_ == "PERSON":
        people.append(ent.text)

print(people)
"""

"""
#a token is basically anything that is in the text, a word or punctuation or anything
#this iwll pring out their part of speech
for token in sentences[1]:
    print(token.text, token.pos_)
"""

"""
#noun chunks are nouns that are governed by other words in the sentence
#some of this is not useful, useful if you want to identify all cases
#where the word watch appears
print(list(doc.noun_chunks))
"""
"""
#try to look for all of the pieces of text that follow this pattern
pattern = [{"POS": "ADV"}, {"POS": "VERB"}]

#extracting verb phrases from the text
verb_phrases = textacy.extract.token_matches(doc, patterns=pattern)

for verb_phrase in verb_phrases:
    print(verb_phrase)
"""


"""

#verbs are inflected, they change basedo n the time or person or other things
#a lemma is the root of a word, example boys = boy, or congratulating = congratulate
#so lemmatizing verbs will help identifying patterns
#can also do this with nouns

for word in sentences[6]:
    if word.pos_ == "VERB":
        print(word, word.lemma_)

"""

#this creates an html object that will display the senteces, different styles
#dep and ent, could also use the serv function, render saves the data
# dep creates a kind of sentence tree that shows the relation ships between words
#the other style option "ent" shows named entity recognition
#this will show what is being grabbed an why
# to customize this to only show one type of entity create a dictionary like
#options = {"ents" = ["Person"]} and pass that in as an options parameter
#like options=options into the render function
html = displacy.render(sentences[6], style="ent")

#that line creates an html file so now we have to save it
with open("dataVis.html", "w") as f:
    f.write(html)
