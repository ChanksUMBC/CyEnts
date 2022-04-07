import spacy
from spacy import displacy
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors


model = KeyedVectors.load_word2vec_format("cyberWordVecWords.txt")
results = model.most_similar(positive=["file"])
print(results)