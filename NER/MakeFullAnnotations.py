#make annotation set with only sentences that have annotations
import json

# each annotator has a pair that annotated the same text that they did
files = ["final_dataset.jsonl"]

for filename in files:

    #load each file as a list of json objects
    file = []
    with open("TrainingData\\" + filename, "r",encoding = "utf-8") as fo:
        json_list = list(fo)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file.append(result)

    i = 0
    while i < len(file):
        if(not file[i]["spans"]):
            file.pop(i)
            i -= 1
        i += 1


    #write to a new jsonl file and the work is done
    with open("TrainingData\\full_dataset.jsonl", "w", encoding="utf-8") as fo:
        for line in file:
            json.dump(line,fo)
            fo.write("\n")