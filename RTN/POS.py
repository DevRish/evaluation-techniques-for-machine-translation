import spacy


class POSDetect:
    def __init__(self):
        # Load a language model (English in this example)
        self.nlp = spacy.load("en_core_web_sm")

    def pos_gen(self, text):
        doc = self.nlp(text)

        nouns = []
        adjectives = []
        articles = []
        verbs = []
        prep = []
        adv = []
        pron = []

        wt_word = {}
        pos_word = {}

        for token in doc:
            if token.pos_ == "NOUN":
                # nouns.append(token.text)
                pos_word[token.text] = "n"
                wt_word[token.text] = 30
            elif token.pos_ == "ADJ":
                # adjectives.append(token.text)
                pos_word[token.text] = "a"
                wt_word[token.text] = 15
            elif token.text.lower() in ["the", "a", "an"]:
                # articles.append(token.text)
                pos_word[token.text] = "t"
                wt_word[token.text] = 1
            elif token.pos_ == "VERB":
                # verbs.append(token.text)
                pos_word[token.text] = "v"
                wt_word[token.text] = 20
            elif token.pos_ == "ADV":
                # adv.append(token.text)
                pos_word[token.text] = "r"
                wt_word[token.text] = 15
            elif token.pos_ == "ADP":
                # prep.append(token.text)
                pos_word[token.text] = "p"
                wt_word[token.text] = 5
            elif token.pos_ == "PRON":
                # pron.append(token.text)
                pos_word[token.text] = "o"
                wt_word[token.text] = 30

        # pos_dict = {"noun": nouns, "adj": adjectives, "art": articles, "verb": verbs}
        return wt_word, pos_word

    def pos_calc(self, text):
        pos_dict = self.pos_gen(text)
        weights = enumerate(["art", "adj", "verb", "noun"], 1)

        wt_word = {l: weights[j] for j, i in pos_dict.items() for l in i}

# Load a language model (English in this example)
# nlp = spacy.load("en_core_web_sm")
#
# text = "i go to the hospital"
# doc = nlp(text)
#
# # Iterate through tokens and extract POS tags
# for token in doc:
#     print(f"Token: {token.text}, POS Tag: {token.pos_, token.dep_}")

# nouns = []
# adjectives = []
# articles = []
# verbs = []
#
# for token in doc:
#     if token.pos_ == "NOUN":
#         nouns.append(token.text)
#     elif token.pos_ == "ADJ":
#         adjectives.append(token.text)
#     elif token.text.lower() in ["the", "a", "an"]:
#         articles.append(token.text)
#     elif token.pos_ == "VERB":
#         verbs.append(token.text)
#
# print("Nouns:", nouns)
# print("Adjectives:", adjectives)
# print("Articles:", articles)
# print("Verbs:", verbs)
