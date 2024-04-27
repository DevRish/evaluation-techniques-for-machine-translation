import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# nltk.download('punkt')
# nltk.download('wordnet')


class Stem:
    def __init__(self):
        # Initialize the Porter stemmer
        self.stemmer = PorterStemmer()

    def stemming(self, a, b):
        if self.stemmer.stem(a) == self.stemmer.stem(b):
            return True
        else:
            return False

    def show(self, a):
        print(self.stemmer.stem(a))


class Lemm:
    def __init__(self):
        # Initialize the WordNet lemmatizer
        self.lemmatizer = WordNetLemmatizer()

    def lemmatizing(self, a, b, posa, posb):
        # f = [self.lemmatizer.lemmatize(x, y) for x, y in a.items()]
        # g = [self.lemmatizer.lemmatize(x, y) for x, y in b.items()]
        if self.lemmatizer.lemmatize(a, posa) == self.lemmatizer.lemmatize(b, posb):
        # if f[0] == g[0]:
        #     if pos == "n":
        #         return 0.85
        #     elif pos == "a":
        #         return 0.8
        #     elif pos == "v":
        #         return 0.55
        #     elif pos == "r":
            return True
        else:
            return False

    def show(self, a):
        print(self.lemmatizer.lemmatize(a, pos="v"))


# s = Stem()
# print(s.stemming("colleges", "college"))
# s.show("Maximus")
# s.show("maximum")
# l = Lemm()
# print(l.lemmatizing({"running": "v"}, {"ran": "v"}))
# # l.show("I am running towards you")
# # l.show("I ran towards you")
# l.show("running")
# l.show("ran")
