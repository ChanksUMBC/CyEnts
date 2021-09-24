import json

#this is a list of all filenames to be converted without .txt or .ann
annoList = ["test"]

#this is the final list that will be output as a json file
annotations = []

for name in annoList:

    #first reaf through the text file and add the text to the list
    filename = name + ".txt"
    with open(filename,"r", encoding="utf-8") as file:
        text = file.read()

        annotations.append([text, {"entities":[]}])

    #then read through .ann file and take out all the information we need
    annoName = name + ".ann"
    with open(annoName,"r", encoding="utf-8") as file:
        for line in file:

            splitLine = line.split("\t")

            labelAndChars = splitLine[1].split(" ")

            label = labelAndChars[0]
            startChar = labelAndChars[1]
            endChar = labelAndChars[2]

            #add the information to the json object
            annotations[-1][1]["entities"].append([label, startChar, endChar])

#dump the json list to a file
with open("cyberAnnotations.json","w",encoding="utf-8") as file:
        json.dump(annotations, file, indent=4, ensure_ascii=False)
