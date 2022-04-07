import pandas as pd
import spacy_annotator as spa
import sys
import spacy
sys.path.append('../')

nlp = spacy.load("en_core_web_md")

df = pd.DataFrame({
    "text": [
        "New york is lovely, Milan is nice, but london is amazing!",
        "Stockholm is too cold. Ingrid Bergman says so."
    ]})

df
annotator = spa.Annotator(labels=["GPE", "PERSON"], model=nlp)
annotator.instructions

df_labels = annotator.annotate(df=df, col_text="text", shuffle=True)

df_labels