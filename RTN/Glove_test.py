import numpy as np
from scipy.spatial.distance import cosine
from gensim.models import KeyedVectors
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
import shutil


class GloveImp():
    def __init__(self):
        # self.glove_file = "C:/Users/ghosh/Downloads/glove.twitter.27B/glove.twitter.27B.200d.txt"
        self.word2vec_glove_file = "glove.twitter.27B.200d.word2vec.txt"
        # glove2word2vec(self.glove_file, self.word2vec_glove_file)
        self.glove_model = KeyedVectors.load_word2vec_format(self.word2vec_glove_file, binary=False, )

    def calc_sim(self, word1, word2):
        similarity = self.glove_model.similarity(word1, word2)
        return (similarity + 1) / 2
        # print(f"Cosine Similarity between '{word1}' and '{word2}': {(similarity + 1) / 2}")

# Load pre-trained GloVe model (Example: 100-dimensional embeddings)
# glove_file = 'C:/Users/ghosh/Downloads/glove.6B/glove.6B.100d.txt'
# glove_file = "C:/Users/ghosh/Downloads/glove.twitter.27B/glove.twitter.27B.200d.txt"

# glove_path = 'C:/Users/ghosh/Downloads/glove.6B/glove.6B.100d.txt'

# glove_model = KeyedVectors.load_word2vec_format(word2vec_glove_file, binary=False, )

# Get word embeddings
# word1 = "cat"
# word2 = "mat"
# # embedding1 = glove_model[word1]
# # embedding2 = glove_model[word2]
#
# # Calculate cosine similarity
# similarity = glove_model.similarity(word1, word2)
#
# print(f"Cosine Similarity between '{word1}' and '{word2}': {(similarity + 1) / 2}")
# print(glove_model.most_similar(word1), glove_model.most_similar(negative=word1))
