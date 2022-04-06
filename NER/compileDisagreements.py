import json

# each annotator has a pair that annotated the same text that they did
file_pairs = [["casey_annotations.jsonl","leyton_annotations.jsonl"],["kate_annotations.jsonl","michael_annotations.jsonl"],["mike_annotations.jsonl","priyanka_annotations.jsonl"]]

newfile = []

for pair in file_pairs:

    #load each file as a list of json objects
    file1 = []
    with open("TrainingData\\DISAGREE" + pair[0], "r",encoding = "utf-8") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file1.append(result)

    file2 = []
    with open("TrainingData\\DISAGREE" + pair[1], "r",encoding = "utf-8") as file:
        json_list = list(file)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file2.append(result)

    
    sentence_num = 0;

    #go through each json object or "sentence"
    while sentence_num < len(file1) and sentence_num < len(file2):

        #make sure they match up
        if(file1[sentence_num]["text"] == file2[sentence_num]["text"]):
            sent1 = file1[sentence_num]["text"]
            sent2 = file2[sentence_num]["text"]

            span1 = file1[sentence_num]["spans"]
            span2 = file2[sentence_num]["spans"]

            len1 = len(span1)
            len2 = len(span2)

            if(len1 != 0 and len2 != 0 ):
                newfile.append("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||" + "\n")
                newfile.append(file1[sentence_num]["text"]+"\n")
                newfile.append("".rjust(35).ljust(38)+ "|" + "".ljust(35).rjust(38) + "\n")
                newfile.append("".rjust(35).ljust(38)+ "|" + "".ljust(35).rjust(38) + "\n")

            
                if(len1 > len2 ):
                    lenF = len1
                else:
                    lenF = len2

                for i in range(lenF):
                    part1 = ""
                    part2 = ""

                    if(i >= len1):
                        pass
                    else:
                        part1 = "{" + sent1[span1[i]["start"] : span1[i]["end"]] + "}" + "->"+span1[i]["label"]
                    
                    part1 = part1.rjust(35).ljust(38)

                    if(i >= len2):
                        pass
                    else:
                        part2 = "{" + sent2[span2[i]["start"] : span2[i]["end"]]+ "}""->"+span2[i]["label"]
                    
                    part2 = part2.ljust(35).rjust(38)
                    
                    newfile.append(part1 + "|" + part2 + "\n")
                    newfile.append("".rjust(35).ljust(38)+ "|" + "".ljust(35).rjust(38) + "\n")
        
        sentence_num += 1

with open("annotation_disagreements.txt", "w", encoding = "utf-16") as file:

    for line in newfile:
        file.write(line)
