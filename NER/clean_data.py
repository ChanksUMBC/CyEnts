import json
import regex as re

def trim_entity_spans(data: list) -> list:
    """Removes leading and trailing white spaces from entity spans.

    Args:
        data (list): The data to be cleaned in spaCy JSON format.

    Returns:
        list: The cleaned data.
    """
    invalid_span_tokens = re.compile(r'\s')

    cleaned_data = []
    for entry in data:
        entities = entry['spans']
        valid_entities = []
        for span in entities:
            valid_start = span["start"]
            valid_end = span["end"]
            while valid_start < len(entry["text"]) and invalid_span_tokens.match(
                    entry["text"][valid_start]):
                valid_start += 1
            while valid_end > 1 and invalid_span_tokens.match(
                    entry["text"][valid_end - 1]):
                valid_end -= 1
            valid_entities.append([valid_start, valid_end, span["label"]])
        cleaned_data.append([entry["text"], {'entities': valid_entities}])

    return cleaned_data


"""Convert entity annotation from spaCy v2 TRAIN_DATA format to spaCy v3
.spacy format."""
import srsly
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin


def convert(lang: str, input_path: Path, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    for text, annot in srsly.read_json(input_path):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)


if __name__ == "__main__":

    data = []
    with open("TrainingData/final_dataset.jsonl","r") as f:
        for line in f:
            data.append(json.loads(line))


    with open("TrainingData/final_dataset_fixed.json", "w") as wf:
        json.dump(trim_entity_spans(data),wf)

    convert("en","TrainingData/final_dataset_fixed.json","TrainingData/final_dataset_fixed.spacy")

