import spacy
import random
import json

def loadData(file):

    with open(file, "r", encoding = "utf-8") as f:
        data = json.load(f)
    return data

def trainSpacy(data, iterations):

    nlp = spacy.blank("en")

    if( "ner" not in nlp.pipe_names ):
        ner = nlp.add_pipe("ner")
    
    for _, annotations in data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])
    
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()

        for itn in range(iterations):

            print("Starting Iteration ", itn)
            random.shuffle(data)
            losses = {}

            for text, annotations in data:

                nlp.update(
                    [text],
                    [annotations],
                    drop = 0.2,
                    sgd = optimizer,
                    losses = losses,
                )
            print(losses)
    return(nlp)


def main():
    
    trainingData = loadData( "TrainingData\\cyberAnnotations.json")
    nlp = trainSpacy(trainingData, 30)
    nlp.to_disk("cyber_model")


if __name__ == "__main__":
    
    main()