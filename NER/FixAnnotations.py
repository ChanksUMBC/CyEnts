import json
import pandas as pd

# each annotator has a pair that annotated the same text that they did
file_pairs = [["casey_annotations.jsonl","leyton_annotations.jsonl"],["kate_annotations.jsonl","michael_annotations.jsonl"],["mike_annotations.jsonl","priyanka_annotations.jsonl"]]

dataset = []

for pair in file_pairs:

    #load each file as a list of json objects
    file1 = []
    with open("TrainingData\\" + pair[0], "r",encoding = "utf-16") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file1.append(result)

    df1 = pd.DataFrame(file1)
    df1 = df1.sort_values(by=["text"])
    # Wrap pattern column in a dictionary
    with open("TrainingData\\FIXED" + pair[0], "w", encoding = "utf-16") as file:
        result = df1.to_json(orient = "records")
        parsed = json.loads(result)
        for item in parsed:
            json.dump(item,file)
            file.write("\n")



    file2 = []
    with open("TrainingData\\" + pair[1], "r",encoding = "utf-16") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file2.append(result)

    df2 = pd.DataFrame(file2)
    df2 = df2.sort_values(by=["text"])
    # Wrap pattern column in a dictionary
    with open("TrainingData\\FIXED" + pair[1], "w", encoding = "utf-16") as file:
        result = df2.to_json(orient = "records")
        parsed = json.loads(result)
        for item in parsed:
            json.dump(item,file)
            file.write("\n")

    
for pair in file_pairs:

    #load each file as a list of json objects
    file1 = []
    with open("TrainingData\\FIXED" + pair[0], "r",encoding = "utf-16") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file1.append(result)

    file2 = []
    with open("TrainingData\\FIXED" + pair[1], "r",encoding = "utf-16") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file2.append(result)

    
    sentence_num = 0;

    #go through each json object or "sentence"
    while sentence_num < len(file1) and sentence_num < len(file2):

        #make sure they match up
        if(file1[sentence_num]["text"] != file2[sentence_num]["text"]):
            
            remove1 = False
            remove2 = True

            for i in range(1, 11):
                if(sentence_num + i < len(file1)):
                    if(file1[sentence_num + i]["text"] == file2[sentence_num]["text"]):
                        remove1 = True
                if(sentence_num + i < len(file2)):
                    if(file1[sentence_num]["text"] == file2[sentence_num + i]["text"]):
                        remove2 = True

            if remove1:
                file1.pop(sentence_num)
                sentence_num -= 1

            elif remove2:
                file2.pop(sentence_num)
                sentence_num -= 1

        sentence_num += 1

    with open("TrainingData\\FIXED" + pair[0], "w", encoding = "utf-8") as file:
        for item in file1:
            json.dump(item,file)
            file.write("\n")

    with open("TrainingData\\FIXED" + pair[1], "w", encoding = "utf-8") as file:
        for item in file2:
            json.dump(item,file)
            file.write("\n")