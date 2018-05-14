import numpy as np


def main():
    ms = MarkovSpeech()


class MarkovSpeech:
    def __init__(self):
        self.pair_counts = {}
        self.word_counts = {}

    def count_corpus(self, corpus):
        pass

    def update_pair_count(self, word1, word2):
        if None in [word1, word2]:
            return

        if word1 in self.word_counts:
            self.word_counts[word1] += 1
        else:
            self.word_counts[word1] = 1

        if word1 not in self.pair_counts:
            self.pair_counts[word1] = {}

        if word2 in pair_counts[word1]:
            pair_counts[word1][word2] += 1
        else:
            pair_counts[word1][word2] = 1

    def normalize_pair_count(self):
        



if __name__ == "__main__":
    main()

