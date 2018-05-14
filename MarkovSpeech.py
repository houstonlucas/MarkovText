import numpy as np
import pickle


# Load object
# with open('backup.pickle', 'rb') as handle:
#     ms = pickle.load(handle)

def main():
    ms = MarkovSpeech()


class MarkovSpeech:
    def __init__(self):
        self.pair_counts = {}
        self.word_counts = {}

    def count_corpus(self, corpus):
        special_chars = list(",.!;?()")
        previous_word = None
        current_word = None

        index = 0
        l = len(corpus)
        while index < l:
            special = None
            end = corpus.find(' ', index)
            if end == -1:
                end = l
            section = corpus[index:end+1]

            for char in special_chars:
                if char in section:
                    special = char
                    break

            if special is not None:
                tokens = self.extract_tokens(section, special)
                for token in tokens:
                    current_word = token
                    self.update_pair_count(previous_word, current_word)
                    previous_word = token
            else:
                current_word = section.strip()
                self.update_pair_count(previous_word, current_word)
                previous_word = section.strip()

            index = end + 1

    def extract_tokens(self, section, special_char):
        index = section.find(special_char)
        tokens = [section[:index].strip(), section[index:].strip()]
        return tokens

    def update_pair_count(self, word1, word2):
        if None in [word1, word2]:
            return

        if word1 in self.word_counts:
            self.word_counts[word1] += 1
        else:
            self.word_counts[word1] = 1

        if word1 not in self.pair_counts:
            self.pair_counts[word1] = {}

        if word2 in self.pair_counts[word1]:
            self.pair_counts[word1][word2] += 1
        else:
            self.pair_counts[word1][word2] = 1

    def normalize_pair_count(self):
        for preceding in self.pair_counts:
            for following in self.pair_counts[preceding]:
                if following in self.word_counts:
                    self.pair_counts[preceding][following] /= float(self.word_counts[following])

    def backup(self):
        with open('backup.pickle', 'wb') as handle:
            pickle.dump(self, handle)


if __name__ == "__main__":
    main()

