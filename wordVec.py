import spacy
from spacy import displacy


# the first thing that we need is training data to be able to create these word vectors
# to do this you need a lot of text separated by sentence into lists and then again
# by words so it will look like [["Hello", " I", "am", "cool"], ["He", " is ", " not", "cool"]]
def prepData():
    articles = []
    stopWords = []

    with open("stopWords.txt", "r") as file:
        for line in file:
            stopWords.append(line.strip().lower())

    with open("fireeyeText.jsonl", "r", encoding="utf-8") as file:
        for line in file:
            articles.append(line.split("\"text\": \"")[1].replace("\"}}", ""))


    nlp = spacy.load("en_core_web_lg")
    doc = nlp(articles[0])

    #separates the text into sentences
    sentences = list(doc.sents)

    data = []
    for sent in sentences:

        sent = str(sent)
        sent = sent[:-1]

        words = sent.split(" ")
        finalWords = []
        
        for word in words:

            if word:
                if word.lower() not in stopWords:    
                    finalWords.append(word)

        if finalWords:
            data.append(finalWords)
            finalWords = []

    print(data)

prepData()