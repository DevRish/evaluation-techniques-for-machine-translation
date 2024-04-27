import time
start_time = time.time()
import math
import numpy as np
from collections import Counter
import copy
# from Glove_test import GloveImp
from POS import POSDetect
from Stemmer import Stem, Lemm
import copy
import string

l = Lemm()


# def calc_prec_or_rec(a, b):
#     """
#     if a == generated text and b == reference text
#     then precision will be returned
#     otherwise
#     recall will be returned
#     """
#     r = sum(a.values())
#     for k in a:
#         if k in b:
#             if a[k] > b[k]:
#                 a[k] = b[k]
#         else:
#             a[k] = 0
#     # print(a)
#     score = sum(a.values()) / r
#     # print(score)
#     return score

# def upto_n(clipped_prec):
#     if not np.nonzero(clipped_prec)[0].size > 0:
#         return [0], 1
#     final_prec = [x for x in clipped_prec if x != 0]
#     len_fin = len(final_prec)
#     return final_prec, max(len_fin, 1)


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
        if len(k.split()) == 1 and k in dp:
            # print(k, dp[k])
            wt_ngram[k] = dp[k][0]
            pos_word[k] = dp[k][1]
        else:
            wt_word, pos_word = pos.pos_gen(k)
            for word in wt_word:
                if word not in dp:
                    dp[word] = [wt_word[word], pos_word[word]]
                    # print(f"Here {word, dp[word]}")
            # print(wt_word)
            # temp = wt_unigram[k]
            # wt_unigram[k] = wt_word[k] * temp
            wt_ngram[k] = wt_ngram[k] * sum(wt_word.values())
    # print(wt_ngram)
    return wt_ngram, pos_word


def g_penalty_func(list_size, n=4):
    if list_size == n:
        return 1
    l = list_size / n
    g_pen = 1 - math.exp(-3 * l)
    # print(g_pen)
    return g_pen


def calculation(a, ap, b, bp, n, dp):
    # print(n)
    # print(a, b)
    b_temp = copy.deepcopy(b)
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

        key = " ".join(i for i in a.keys()) + " ".join(i for i in b_temp.keys())
        dp[key] = [total / sum(a.values())]
        return total / sum(a.values())
    elif " ".join(i for i, j in a.items()) + " ".join(i for i, j in b.items()) in dp:
        # print("used")
        return dp[" ".join(i for i, j in a.items()) + " ".join(i for i, j in b.items())][0]
    r = sum(a.values())
    # print(a, r)
    temp = copy.deepcopy(b)
    for k in a:
        if k in b:
            if a[k] > b[k]:
                a[k] = b[k]
            del b[k]

        elif not b:
            b = copy.deepcopy(temp)
            total = 1

            x = 0

            # print(f"{k} Here1")
            f, fp = pos_weightage(k, n - 1, dp)
            # print(f, fp)
            for d in b:
                # print(f"{d} Here2")
                j, jp = pos_weightage(d, n - 1, dp)
                # print(f, j)
                calc = calculation(f, fp, j, jp, n - 1, dp)

                x += 1
                total *= calc

                del b[d]
                break

            a[k] = total * a[k]

        else:
            total = 1

            x = 0

            # print(f"{k} Here1")
            f, fp = pos_weightage(k, n - 1, dp)
            # print(f, fp)
            for d in b:
                # print(f"{d} Here2")
                j, jp = pos_weightage(d, n - 1, dp)
                # print(f,j)
                calc = calculation(f, fp, j, jp, n - 1, dp)

                x += 1
                total *= calc

                del b[d]
                break

            a[k] = total*a[k] #max(total, lesser_total)
            # print(k, a[k])
    key = " ".join(i for i in a.keys()) + " ".join(i for i in b_temp.keys())
    # print(a, sum(a.values()), r)
    dp[key] = [(sum(a.values())) / r if r != 0 else 0]
    # print(dp)
    return (sum(a.values())) / r if r != 0 else 0

def s_score(reference, generated):
    """
    Modified Bleu score function is given the reference, or original text, and generated/machine-translated texts.
    Uses both precision and recall
    """
    gen_length = len(generated.split())
    ref_length = len(reference.split())
    no_red_len = len(set(generated.split()))

    #Redundancy penalty
    red = no_red_len/gen_length


    # Brevity Penalty
    if gen_length > ref_length:
        BP = 1
    else:
        penalty = 1 - (ref_length / gen_length)
        BP = np.exp(penalty)

    n = min(5, gen_length, ref_length)  # upto which n-gram
    dp = {}
    r, rp = pos_weightage(reference, n, dp)
    c1, cp1 = pos_weightage(generated, n, dp)
    r2, rp2 = copy.deepcopy(r), copy.deepcopy(rp)
    c2, cp2 = copy.deepcopy(c1), copy.deepcopy(cp1)
    # print(c1, r)
    precision_score = calculation(c1, cp1, r, rp, n, dp)
    # print(dp)
    recall_score = calculation(r2, rp2, c2, cp2, n, dp)
    # for i in range(1, min(gen_length + 1, n + 1)):
    #     if i == 1:
    #         ref_n_gram = pos_weightage(reference)
    #         gen_n_gram = pos_weightage(generated)
    #     else:
    #         ref_n_gram = Counter(generate_ngram(reference, i))
    #         gen_n_gram = Counter(generate_ngram(generated, i))
    #
    #     # ref_n_gram3 = Counter(generate_ngram(reference, i))
    #     # gen_n_gram3 = Counter(generate_ngram(generated, i))
    #
    #     ref_n_gram2 = copy.deepcopy(ref_n_gram)
    #     gen_n_gram2 = copy.deepcopy(gen_n_gram)
    #
    #     # Calculating the recall (giving more weightage to uni-gram now)
    #     if i == 1:
    #         recall_score.append(calc_prec_or_rec(ref_n_gram2, gen_n_gram2, ))
    #     else:
    #         recall_score.append(calc_prec_or_rec(ref_n_gram2, gen_n_gram2, ))
    #
    #     # Calculating the clipped-precision (giving more weightage to uni-gram now)
    #     if i == 1:
    #         clipped_precision_score.append(calc_prec_or_rec(gen_n_gram, ref_n_gram, ))
    #     else:
    #         clipped_precision_score.append(calc_prec_or_rec(gen_n_gram, ref_n_gram, ))

    print(precision_score, recall_score)
    # print(recall_score)
    # final_prec, l1 = upto_n(clipped_precision_score)  # fetches a list of non-zero BLEU scores and also the length
    # final_rec, l2 = upto_n(recall_score)  # fetches a list of non-zero BLEU scores and also the length
    # g_penalty_prec = g_penalty_func(l1, n)
    # g_penalty_rec = g_penalty_func(l2, n)
    # of that list so the weight can be calculated
    # weights = [0.5] * 2  # Modifying for bleu-2, would be [0.25]*4 for bleu-4     <-----Not a useful way
    # s = (w_i * math.log(p_i) for w_i, p_i in zip(weights, clipped_precision_score))     of calculating BLEU score
    # s = BP * math.exp(math.fsum(s))
    # wt_prec = 1 / (l1)
    # wt_rec = 1 / (l2)
    # global_avg_prec1 = (math.prod(final_prec) ** wt_prec)
    # global_avg_rec1 = (math.prod(final_rec) ** wt_rec)
    # global_avg_prec = g_penalty_prec * (math.prod(final_prec) ** wt_prec)
    # global_avg_rec = g_penalty_rec * (math.prod(final_rec) ** wt_rec)
    if precision_score == 0 or recall_score == 0:
        return 0
    else:
        precision_score = precision_score * red * BP
        f1_score = (2 * precision_score * recall_score) / (precision_score + recall_score)
    # print(f"Precision and recall without considering g-penalty:{global_avg_prec1, global_avg_rec1}")
    # print(f"Precision and recall after considering g-penalty:{global_avg_prec, global_avg_rec}")
    # print(f1_score)
    # s = BP * f1_score
    # print(f"Original bleu-score: {BP * global_avg_prec1}")
    return f1_score
    # return recall_score

reference = 'I go to the school'
sent2 = "I go to a school"
sent3 = "I go in the school"
sent4 = "I go to the schools"
sent5 = "I eat to the school"
sent6 = "I going to the school"
sent7 = "I go to the college"
sent13 = "You go to the school"
sent8 = "I go"
sent9 = "I go to school"
sent10 = "I go the school"
sent14 = "I I go go to to the the school"
sent15 = "I go to the school I go to the school"
sent11 = "I play the guitar in school"
sent16 = "To I go school the"
sent12 = "I go to the school in a bus"
sent17 = "I go to an institution for learning"
sent18 = "He comes from cinema"
# reference2 = input("Type reference translation: ").translate(str.maketrans('', '', string.punctuation))
# candidate = input("Type candidate translation: ").translate(str.maketrans('', '', string.punctuation))
print(f"S-score: {sent2, s_score(reference, sent2)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent3, s_score(reference, sent3)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent4, s_score(reference, sent4)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent5 ,s_score(reference, sent5)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent6, s_score(reference, sent6)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent7, s_score(reference, sent7)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent13, s_score(reference, sent13)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent8, s_score(reference, sent8)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent9, s_score(reference, sent9)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent14, s_score(reference, sent14)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent15,s_score(reference, sent15)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent10, s_score(reference, sent10)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent11, s_score(reference, sent11)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent16, s_score(reference, sent16)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent12, s_score(reference, sent12)}")
print("--- %s seconds ---" % (time.time() - start_time))
print(f"S-score: {sent17, s_score(reference, sent17)}")
# print(f"S-score: {candidate, s_score(reference, candidate)}")
print("--- %s seconds ---" % (time.time() - start_time))
