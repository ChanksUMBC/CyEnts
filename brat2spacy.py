import json

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
"80-to-0-in-under-5-seconds-falsifying-a-medical-patients-vitals$$PART5",]

#this is the final list that will be output as a json file
annotations = []

for name in annoList:

    #first read through the text file and add the text to the list
    filename = "FinishedAnnotations\\"+ name + ".txt"
    with open(filename,"r", encoding="utf-8") as file:
        text = file.read()

        annotations.append([text, {"entities":[]}])

    #then read through .ann file and take out all the information we need
    annoName = "FinishedAnnotations\\"+ name + ".ann"
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
with open("TrainingData/cyberAnnotations.json","w",encoding="utf-8") as file:
        json.dump(annotations, file, indent=4, ensure_ascii=False)