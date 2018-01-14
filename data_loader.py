import os

from hazm.Normalizer import Normalizer

norm = Normalizer(punctuation_spacing=True)


def make_ngram(word, size):
    if size > len(word):
        raise StopIteration
    for i in range(len(word) - size + 1):
        yield word[i:i + size]


def make_ngrams(sizes: list):
    ROOT = "/home/hassan/PycharmProjects/sentiment_lab/attempt04/train"
    max_word_len = -1
    for f in os.listdir(ROOT):
        abs_path = os.path.join(ROOT, f)
        for line in open(abs_path, "r"):

            for word in norm.normalize(line.replace("-", " - ")).split(" "):
                ngrams = []
                if len(word) > max_word_len:
                    print(word)
                max_word_len = max(len(word), max_word_len)
                for size in sizes:
                    ngrams = ngrams + list(make_ngram(word, size))
                    yield max_word_len, ngrams, word


def load_data(sizes):
    ngrams = set()
    max_word_len = 0
    for max_w_len, ngrams, word in make_ngrams(sizes):
        max_word_len = max_w_len
        # ngrams.add(new_ngram)
        print(word, ngrams)
    return max_word_len, ngrams


print(load_data([2, 3, 4])[0])
