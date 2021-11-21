import spacy

nlp = spacy.load("en_core_web_lg")
text = ""

linkList= []
sources = ["fireeye", "fortinet", "ibm", "juniper", "kapersky", "mcAfee", "recordedFuture"]
for source in sources:
    filepath = "cyberJson\\"+source+"Text.jsonl"
    #obtains the text from the json format removing the curly braces and such
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            text = line.split("\"text\": \"")[1].replace("\"}}", "")
            link = line.split("\": {")[0].replace("{", "")

            #print(link)
            doc = nlp(text, disable = ['ner'])

            #separates the text into sentences
            sentences = list(doc.sents)

            title = link.split("/")[-1].replace(".","@")
            if not title:
                title = link.split("/")[-2].replace(".","@")
            sentPath = "Sentences\\" + title + ".txt"

            linkList.append(sentPath)

            with open(sentPath,"w",encoding="utf-8") as sentenceFile:
                for sent in sentences:
                    #print("8888888888888888888888888888888888888888888888888888888888888")
                    #print(sent)
                    sentenceFile.write(str(sent))
                    sentenceFile.write("\n")
                    sentenceFile.write("\n")

with open("sentenceSources.txt", "w", encoding = "utf-8") as file:
    for link in linkList:
        file.write(link)
        file.write("\n")

