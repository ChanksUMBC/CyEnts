ENTIRE_LINE = 0
ENTITIES = 1
START = 0
END = 1
LABEL = 2
ENTIRE = 3

#each annotator has a pair that annotated the same text that they did
file_pairs = [["annotations.jsonl","annotationsSecond.jsonl"]]

dataset = []

for pair in file_pairs:

    #for each annotator extract the key information about what they annotated
    file1 = []
    with open("AnnotatorCollections\\" + pair[0], "r",encoding = "utf-16") as file:

        newline = []
        for line in file:
            if line != "\n":

                newline.append(line)

                #this takes just the annotated entities from the info
                entities = line.split("\"spans\":[")[1].split(",\"_is_binary\"")[0][1:].split("}")[:-1]
                everything_else = line.split("\"spans\":[")[0] + "INSERTHERE" + line.split(",\"_is_binary\"")[1]

                for entity in entities:
                    if(entity != ""):
                        #for each entity we want to know where it starts, ends, and what type it is
                        char_counter = []
                        entity = entity.replace(",{","")
                        counting = entity.split("\"start\":")[1]
                        count = counting.split(",\"end\":")

                        #this finds the start and end and type
                        char_counter.append(count[0])
                        char_counter.append(count[1].split(",\"")[0])
                        entity_type = entity.split("\"label\":\"")[1][:-1]

                        #not everything is consistent so this is to account for inconsistencies in the format
                        if(len(entity_type) > 20):
                            entity_type = entity_type.split("\",\"source")[0]

                        char_counter.append(entity_type)
                        char_counter.append(entity)
                        print(char_counter , "\n")

                        newline.append(char_counter)

        file1.append(newline)
        #now file1 is in the format of
        #[ [entireline1, [1,2,GPE,ORIGINALTEXT], [3,4,GOV,ORIGINALTEXT] ], [ entirelline2, [1,2,GPE,ORIGINALTEXT] ] ... ]
    
    file2 = []
    with open("AnnotatorCollections\\" + pair[0], "r",encoding = "utf-16") as file:

        newline = []
        for line in file:
            if line != "\n":

                newline.append(line)

                #this takes just the annotated entities from the info
                entities = line.split("\"spans\":[")[1].split(",\"_is_binary\"")[0][1:].split("}")[:-1]

                for entity in entities:
                    if(entity != ""):

                        #for each entity we want to know where it starts, ends, and what type it is
                        char_counter = []
                        entity.replace("{","")
                        counting = entity.split("\"start\":")[1]
                        count = counting.split(",\"end\":")

                        #this finds the start and end and type
                        char_counter.append(count[0])
                        char_counter.append(count[1].split(",\"")[0])
                        entity_type = entity.split("\"label\":\"")[1][:-1]

                        #not everything is consistent so this is to account for inconsistencies in the format
                        if(len(entity_type) > 20):
                            entity_type = entity_type.split("\",\"source")[0]

                        char_counter.append(entity_type)

                        newline.append(char_counter)

        file2.append(newline)
        #now file1 is in the format of
        #[ [entireline1, [1,2,GPE], [3,4,GOV] ], [ entirelline2, [1,2,GPE] ] ... ]
        
    