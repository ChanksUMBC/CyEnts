import json

# each annotator has a pair that annotated the same text that they did
files = ["final_dataset.jsonl","FIXEDcasey_annotations.jsonl","FIXEDleyton_annotations.jsonl","FIXEDkate_annotations.jsonl","FIXEDmichael_annotations.jsonl","FIXEDmike_annotations.jsonl","FIXEDpriyanka_annotations.jsonl"]

for filename in files:

    num_sents = 0
    num_sents_annotated = 0
    num_annotations = 0
    entity_numbers = {}

    #load each file as a list of json objects
    file = []
    with open("TrainingData\\" + filename, "r",encoding = "utf-8") as fo:
        json_list = list(fo)

        for json_dict in json_list:
            result = json.loads(json_dict)
            file.append(result)

    for line in file:
        num_sents += 1
        if(line["spans"]):
            num_sents_annotated += 1

            for entity in line["spans"]:
                num_annotations += 1
                if(entity_numbers.get(entity["label"],0)):
                    entity_numbers[entity["label"]] += 1

                else:
                    entity_numbers[entity["label"]] = 1

    print()
    print("||**||**||**||**||**||**||**||**||**||**||**||**||**||**||**||**||**||")
    print()
    print("------------------", filename.upper(), "------------------")
    print()
    print("Number of Sentences: ", num_sents)
    print()
    print("Number of Sentences With Annotations: ", num_sents_annotated)
    print()
    print("Number of Entities Annotated: ", num_annotations)
    print()
    print("Counts for each entitiy type:")
    print(entity_numbers)
    print()
    print("||**||**||**||**||**||**||**||**||**||**||**||**||**||**||**||**||**||")
    print()