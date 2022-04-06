import json
from spacy.tokens import DocBin
import spacy
from spacy.util import load_config
from tqdm import tqdm
import random

#this is a list of all filenames to be converted without .txt or .ann
annoList = ["shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems$$PART1",
"shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems$$PART2",
"shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems$$PART3",
"shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems$$PART4"
,"shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems$$PART5",
"shining-a-light-on-darkside-ransomware-operations@html$$PART1",
"shining-a-light-on-darkside-ransomware-operations@html$$PART2",
"shining-a-light-on-darkside-ransomware-operations@html$$PART3",
"shining-a-light-on-darkside-ransomware-operations@html$$PART4",
"shining-a-light-on-darkside-ransomware-operations@html$$PART5",
"abusing-replication-stealing-adfs-secrets-over-the-network@html$$PART1",
"abusing-replication-stealing-adfs-secrets-over-the-network@html$$PART2",
"abusing-replication-stealing-adfs-secrets-over-the-network@html$$PART3",
"abusing-replication-stealing-adfs-secrets-over-the-network@html$$PART4",
"abusing-replication-stealing-adfs-secrets-over-the-network@html$$PART5",
"80-to-0-in-under-5-seconds-falsifying-a-medical-patients-vitals$$PART1",
"80-to-0-in-under-5-seconds-falsifying-a-medical-patients-vitals$$PART2",
"80-to-0-in-under-5-seconds-falsifying-a-medical-patients-vitals$$PART3",
"80-to-0-in-under-5-seconds-falsifying-a-medical-patients-vitals$$PART4",
"80-to-0-in-under-5-seconds-falsifying-a-medical-patients-vitals$$PART5",
"cool"]


def main():
    #brat2spacy2()
    data = loadData()
    random.shuffle(data)
    doc = createTrainingData(data)
    doc.to_disk("./TrainingData/cyberTraining.spacy")


def createTrainingData(TRAIN_DATA):

    nlp = spacy.blank("en")
    db = DocBin()

    for text, annot in TRAIN_DATA:
        doc = nlp.make_doc(text)
        ents = []

        for label, start, end in annot["entities"]:
            span = doc.char_span(int(start), int(end), label = label, alignment_mode="contract")
            
            if span is None:
                pass
                print("Skipping")

            else:
                if(label == "Todd"):
                    print(start,end,label)
                    print(span.text)
                ents.append(span)
        doc.ents = ents
        db.add(doc)

    return(db)


def loadData():
    with open("./TrainingData/cyberAnnotations.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
    return data

def brat2spacy2():
    """
    Brat's default annotation format includes the start and end characters
    it starts at 0 and includes the character after the final character of the annotation
    it also counts new line characters "\n" in it's count and will count that as 
    2 towards the total character count
    Brat also does not have wraparound so if you try to do it before the annotation process
    then you just get dunked on.
    """
    #this is the final list that will be returned to be used later
    annotations = []

    for name in annoList:

        #first read through the text file and add the text to the list
        filename = ".\\FinishedAnnotations\\"+ name + ".txt"
        with open(filename,"r", encoding="utf-8") as file:
            text = file.read()
            annotations.append([text, {"entities":[]}])

        #then read through .ann file and take out all the information we need
        annoName = ".\\FinishedAnnotations\\"+ name + ".ann"
        with open(annoName,"r", encoding="utf-8") as file:
            for line in file:

                splitLine = line.split("\t")

                labelAndChars = splitLine[1].split(" ")

                label = labelAndChars[0]
                startChar = int(labelAndChars[1])
                endChar = int(labelAndChars[2])

                #add the information to the json object
                annotations[-1][1]["entities"].append([label, startChar, endChar])

        with open("./TrainingData/cyberAnnotations.json", "w", encoding = "utf-8") as file:
            json.dump(annotations, file, indent=4, ensure_ascii=False)

    return annotations

if __name__ == "__main__":
    main()



