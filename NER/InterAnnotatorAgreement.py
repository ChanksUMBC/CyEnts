import json
import copy

# each annotator has a pair that annotated the same text that they did
file_pairs = [["casey_annotations.jsonl","leyton_annotations.jsonl"],["kate_annotations.jsonl","michael_annotations.jsonl"],["mike_annotations.jsonl","priyanka_annotations.jsonl"]]

dataset = []

for pair in file_pairs:

    #load each file as a list of json objects
    file1 = []
    with open("TrainingData\\FIXED" + pair[0], "r",encoding = "utf-8") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file1.append(result)

    file2 = []
    with open("TrainingData\\FIXED" + pair[1], "r",encoding = "utf-8") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file2.append(result)

    
    sentence_num = 0;
    disagree1 = copy.deepcopy(file1)
    disagree2 = copy.deepcopy(file2)

    #go through each json object or "sentence"
    while sentence_num < len(file1) and sentence_num < len(file2):

        #make sure they match up
        if(file1[sentence_num]["text"] == file2[sentence_num]["text"]):
            
            ann_num1 = 0;
            ann_num2 = 0;
            entities1 = file1[sentence_num]["spans"]
            entities2 = file2[sentence_num]["spans"]
            validEntities = []
            validEntities2 = []

            #if both have entities that were annotated
            if(entities1 and entities2):

                #go through each and compare them
                while ann_num1 < len(entities1) and ann_num2 < len(entities2):

                    #if they have matching starts ends and labels, they are the same so they are valid
                    if(entities1[ann_num1]["start"] == entities2[ann_num2]["start"]):
                        if(entities1[ann_num1]["end"] == entities2[ann_num2]["end"]):
                            if(entities1[ann_num1]["label"] == entities2[ann_num2]["label"]):

                                validEntities.append(entities1[ann_num1])
                                validEntities2.append(entities2[ann_num2])
                        
                        ann_num2 += 1
                        ann_num1 += 1
                    
                    #else we can move onto the next two to compare each other
                    #making sure to compare all those that can be reasonably the same
                    elif(entities1[ann_num1]["start"] < entities2[ann_num2]["start"]):
                        
                        ann_num1 += 1
                    
                    else:
                        ann_num2 += 1
                
                #replace old entitites with valid ones
                #then add it tot he dataset
                file1[sentence_num]["spans"] = validEntities
                dataset.append(file1[sentence_num])

                remove1 = []
                i = 0
                for entity in disagree1[sentence_num]["spans"]:
                    for other in validEntities:
                        if(entity == other):
                            remove1.append(i)
                    i += 1

                i = 0
                for index in remove1:
                    disagree1[sentence_num]["spans"].pop(index - i)
                    i += 1


                remove2 = []
                i = 0
                for entity in disagree2[sentence_num]["spans"]:
                    for other in validEntities2:
                        if(entity == other):
                            remove2.append(i)
                    i += 1

                i = 0
                for index in remove2:
                    disagree2[sentence_num]["spans"].pop(index - i)
                    i += 1

            
            #determine what to do with sentences that were not annotated
            if(entities2 and not entities1):
                dataset.append(file1[sentence_num])

            elif(entities1 and not entities2):
                dataset.append(file2[sentence_num])

            elif(not entities2 and not entities1):
                dataset.append(file2[sentence_num])

        else:
            print("Something went wrong, files are not the same")

        sentence_num += 1

    with open("TrainingData\\DISAGREE" + pair[0], "w", encoding="utf-8") as file:
        for line in disagree1:
            json.dump(line,file)
            file.write("\n")

    with open("TrainingData\\DISAGREE" + pair[1], "w", encoding="utf-8") as file:
        for line in disagree2:
            json.dump(line,file)
            file.write("\n")
    
#write to a new jsonl file and the work is done
with open("TrainingData\\final_dataset.jsonl", "w", encoding="utf-8") as file:
    for line in dataset:
        json.dump(line,file)
        file.write("\n")


    