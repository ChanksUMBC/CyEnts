import json

with open("AnnotatorCollections\\annotations.jsonl", "r") as file:
    for line in file:
        dictionary = dict(line)
        print(dictionary)

