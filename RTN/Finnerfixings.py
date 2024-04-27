import math
import numpy as np
from collections import Counter
from POS import POSDetect
from Stemmer import Stem, Lemm
import copy

s = Stem()
l = Lemm()


def generate_ngram(text, n=2, n_gram=False):
    """
    N-Gram generator with parameters sentence
    n is for the number of n_grams
    The n_gram parameter removes repeating n_grams
    """
    text = text.lower()  # converting to lower case
    str_arr = np.array(text.split())  # split to string arrays
    length = len(str_arr)

    word_list = []
    for i in range(length + 1):
        if i < n:
            continue
        word_range = list(range(i - n, i))
        s_list = str_arr[word_range]
        string = ' '.join(s_list)  # converting list to strings
        word_list.append(string)  # append to word_list
        if n_gram:
            word_list = list(set(word_list))
    return word_list


def pos_weightage(text, n, dp):
    """Provide a weightage on a scale of 1-4 for each POS as follows:
        Noun : 4
        Verb : 3
        Adj : 2
        Article : 1
       Thus generating a weighted uni-gram """
    text = text.lower()
    pos = POSDetect()
    # wt_word = pos.pos_gen(text)
    # print(wt_word)
    # print(n)
    wt_ngram = Counter(generate_ngram(text, n))
    pos_word = {}
    # print(f"{wt_ngram} HERE")
    for k in wt_ngram:
        if k in dp:
            wt_ngram[k] = dp[k][0]
            pos_word[k] = dp[k][1]
        else:
            wt_word, pos_word = pos.pos_gen(k)
            for word in wt_word:
                if word not in dp:
                    dp[word] = [wt_word[word], pos_word[word]]
            # print(wt_word)
            # temp = wt_unigram[k]
            # wt_unigram[k] = wt_word[k] * temp
            wt_ngram[k] = wt_ngram[k] * sum(wt_word.values())
    # print(wt_ngram)
    return wt_ngram, pos_word


def calculation(a, ap, b, bp, n, dp):
    # print(n)
    # print(a, b)
    if n == 1:
        total = 0
        for k in a:
            # print(k, ap[k])
            if k in b:
                # print(k, ap[k])
                total += a[k]
                del b[k]
                del bp[k]
            elif ap[k] in ["a", "v", "n", "r"]:
                for h in b:
                    # print(k, ap[k], h, bp[h])
                    # print(l.lemmatizing(k, h, ap[k], bp[h]))
                    if bp[h] in ["a", "v", "n", "r"]:
                        if l.lemmatizing(k, h, ap[k], bp[h]):
                            if ap[k] == "n":
                                total += 0.8 * a[k]
                            elif ap[k] == "a" or ap[k] == "r":
                                total += 0.85 * a[k]
                            elif ap[k] == "v":
                                total += 0.75 * a[k]
                    # print(total)

        key = " ".join(i for i in a.keys()) + " ".join(i for i in b.keys())
        dp[key] = [total / sum(a.values())]
        return total / sum(a.values())
    elif " ".join(i for i, j in a.items()) + " ".join(i for i, j in b.items()) in dp:
        # print("used")
        return dp[" ".join(i for i, j in a.items()) + " ".join(i for i, j in b.items())][0]
    r = sum(a.values())
    # print(a, r)
    for k in a:
        if k in b:
            if a[k] > b[k]:
                a[k] = b[k]
            del b[k]
        else:
            total = 1
            lesser_total = 1
            lesser_x = 0
            x = 0
            temp = 0
            # print(f"{k} Here1")
            f, fp = pos_weightage(k, n - 1, dp)
            # print(f, fp)
            for d in b:
                # print(f"{d} Here2")
                j, jp = pos_weightage(d, n - 1, dp)
                # print(j)
                calc = calculation(f, fp, j, jp, n - 1, dp)

                if calc > temp and calc > 0.33:
                    x += 1 #if calc > 0.33 else 0
                    total *= calc #if calc > 0.33 else 1
                    temp = calc
                elif calc > 0:
                    lesser_x += 1
                    lesser_total *= calc
                # temp = calc
                if x > 0:
                    # print(total)
                    if total ** (1 / x) > 0.80:
                        break

                # print(total)
            # print(f)
            lesser_total = (lesser_total ** (1 / lesser_x)) * a[k] if lesser_x > 0 else 0
            total = (total ** (1 / x)) * a[k] if x > 0 else 0
            # print(total, lesser_total)
            a[k] = max(total, lesser_total)
    key = " ".join(i for i in a.keys()) + " ".join(i for i in b.keys())
    dp[key] = [(sum(a.values())) / r if r != 0 else 0]
    print(dp)
    return (sum(a.values())) / r if r != 0 else 0


sent1 = "i go to the school"
sent2 = "i go to the schools"
sent3 = "i going to the school"
sent4 = "I play the guitar in school"
sent5 = "I go to the hospital"
sent6 = "I go the school"
dp = {}
n = 5
r, rp = pos_weightage(sent1, n, dp)
r1, rp1 = copy.deepcopy(r), copy.deepcopy(rp)
r2, rp2 = copy.deepcopy(r), copy.deepcopy(rp)
r3, rp3 = copy.deepcopy(r), copy.deepcopy(rp)
r4, rp4 = copy.deepcopy(r), copy.deepcopy(rp)
r5, rp5 = copy.deepcopy(r), copy.deepcopy(rp)
r6, rp6 = copy.deepcopy(r), copy.deepcopy(rp)
c1, cp1 = pos_weightage(sent2, n, dp)
c2, cp2 = pos_weightage(sent3, n, dp)
c3, cp3 = pos_weightage(sent4, n, dp)
c4, cp4 = pos_weightage(sent5, n, dp)
c5, cp5 = pos_weightage(sent6, n, dp)
# print(calculation(c1, cp1, r, rp, 5, dp))
# print(calculation(c2, cp2, r1, rp1, 5, dp))
# print(calculation(c3, cp3, r2, rp2, 5, dp))
# print(calculation(c4, cp4, r5, rp5, 5, dp))
print(calculation(c5, cp5, r6, rp6, 5, dp))
# print(calculation(r4, rp4, r3, rp3, 5, dp))