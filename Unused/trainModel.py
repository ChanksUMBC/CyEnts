import spacy
import random
import json
from spacy.training import Example
from spacy.tokens import Doc

def loadData(file):

    data = []
    with open(file, "r", encoding = "utf-8") as f:
        
        for l in f:
            line_data = {"text":"","entities":[]}
            line = json.loads(l)
            line_data["text"] = line["text"]
            for ent in line["spans"]:
                ent_data = [ent["start"],ent["end"],ent["label"]]
                line_data["entities"].append(ent_data)
            data.append(line_data)
    return data

def trainSpacy(data, iterations):

    nlp = spacy.load("CyEnts_model")

    if( "ner" not in nlp.pipe_names ):
        ner = nlp.add_pipe("ner")
    
    """for _, annotations in data:
        for ent in annotations.get("entities"):
            print(ent)
            ner.add_label(ent[2])"""
    
    examples = []
    for document in data:

        doc = nlp(document["text"])
        example = Example.from_dict(doc, {"entities": document["entities"]})
        examples.append(example)
    

    n_iter = 20
    optimizer = nlp.create_optimizer()

    for i in range(n_iter):
        losses = {}
        random.shuffle(examples)

        for example in examples:

            nlp.update([example], sgd=optimizer, losses=losses,drop=0.01)
        print('Loss at iteration', i, ':', losses['ner'])
    return(nlp)


def main():
    
    trainingData = loadData( "TrainingData\\final_dataset.jsonl")
    nlp = trainSpacy(trainingData, 30)
    nlp.to_disk("CyEnts_Model_trained")


if __name__ == "__main__":
    
    main()