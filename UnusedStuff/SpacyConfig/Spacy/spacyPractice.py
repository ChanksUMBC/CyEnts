import spacy
from spacy import displacy
from spacytextblob.spacytextblob import SpacyTextBlob
import coreferee

nlp = spacy.load("en_core_web_md")
nlp.add_pipe('spacytextblob')

nlp.add_pipe('coreferee')




"""
text = "The European Union has unveiled some of the world's most ambitious proposals to reduce carbon emissions and wean its 27 members off fossil fuels, including taxes on emissions-heavy imports into the union and non-renewable energy, such as oil, gas and coal. The package of measures looks to fundamentally transform the world's single largest trading bloc. It touches on almost every area of economic activity -- from how citizens heat their homes and commute, to a total upheaval of manufacturing practices."

doc = nlp(text)

for sentence in doc.sents:
    print(sentence)

displacy.render(doc, style="dep")
displacy.render(doc, style="ent")

for entity in doc.ents:
    print(f" Entity: {entity.text}, {entity.label_}")
for np in doc.noun_chunks:
    print(f" NP: {np.text}")
"""




"""

doc1 = nlp("A mouse ate my cheese.")
doc2 = nlp("Some cheese was eaten by a rodent!")
doc3 = nlp("All of the cheddar was eaten by rats!")
doc4 = nlp("Computers can analyze language today.")
print(f"Similarity of docs 1 and 2: {doc1.similarity(doc2):.2f}")
print(f"Similarity of docs 1 and 3: {doc1.similarity(doc3):.2f}")
print(f"Similarity of docs 1 and 4: {doc1.similarity(doc4):.2f}")


doc1 = nlp("Alice killed Bob")
doc2 = nlp("Bob killed Alice")
print(f"Similarity of doc1 and doc2: {doc1.similarity(doc2):.2f}")


### SpaCY has multiple language models and even the medium one knows when people are similar

doc1 = nlp("Jennifer Aniston")
doc2 = nlp("Brad Pitt")
doc3 = nlp("Marie Currie")

print(f"Similarity of Jennifer Aniston and Brad Pitt: {doc1.similarity(doc2):.2f}")
print(f"Similarity of Marie Currie and Brad Pitt: {doc3.similarity(doc2):.2f}")

"""




"""
#then import textblob

doc = nlp("I hated calculus 2 and had a difficult time. I didn't like the course and got a bad grade.")
print(f"Polarity: {doc._.polarity:.2f}")         # -1 to +1
print(f"Subjectivity: {doc._.subjectivity:.2f}") # 0 to 1.0 with 0 for rational and 1 for emotional
print(f"Assesments: {doc._.assessments}")        # words that indicate the sentiment


doc = nlp("Tesla's Model 3 is worth the price.")
print(f"Polarity: {doc._.polarity:.2f}")         # -1 to +1
print(f"Subjectivity: {doc._.subjectivity:.2f}") # foo
print(f"Assesments: {doc._.assessments}")        # bar

doc = nlp("The store will open at 9:00 am and close at 5:00 pm.")
print(f"Polarity: {doc._.polarity:.2f}")         # -1 to +1
print(f"Subjectivity: {doc._.subjectivity:.2f}") # foo
print(f"Assesments: {doc._.assessments}")        # bar
"""

doc = nlp("""Although he was very busy with his work, Peter Piper had had enough of it. \
He and his wife decided they needed a holiday. They travelled to Spain because \
she loved the country very much.""")

doc._.coref_chains.print()

doc = nlp("""APT41 is a state-sponsored espionage group. It is based in China and attacks \
higher education, travel services and media firms from that country.""")
print(f"Named entities: {doc.ents}")
print(f"Noun chunks: {[np for np in doc.noun_chunks]}")
print("\nCoreference chains:")
doc._.coref_chains.print()