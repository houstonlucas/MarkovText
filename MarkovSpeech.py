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
        if word1 in self.word_counts:
            self.word_counts[word1] += 1
        else:
            self.word_counts[word1] = 1

        if word2 in self.pair_counts[word1]:
            self.pair_counts[word1][word2] += 1
        else:
            self.pair_counts[word1][word2] = 1


if __name__ == "__main__":
    main()

