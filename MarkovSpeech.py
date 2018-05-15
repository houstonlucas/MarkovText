import numpy as np
import pickle


# Load object
# with open('backup.pickle', 'rb') as handle:
#     ms = pickle.load(handle)

def main():
    ms = MarkovSpeech()

    with open("corpus_lotr", 'r') as f:
        text = f.read()
    ms.count_corpus(text)
    ms.normalize_pair_count()
    text = ms.generate_text(8)
    print(text)


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
                self.pair_counts[preceding][following] /= float(self.word_counts[preceding])

    def backup(self):
        with open('backup.pickle', 'wb') as handle:
            pickle.dump(self, handle)

    def generate_text(self, num_sentences):
        text = ""
        previous = "."
        for i in range(num_sentences):
            sentence = ""
            start = True
            while start or not previous in ".;?!":
                start = False
                next_words, probs = zip(*self.pair_counts[previous].items())
                next_word = np.random.choice(next_words, p=probs)
                previous = next_word

                filler = "" if next_word in ".,;?!" else " "
                sentence += filler + next_word
            text += sentence + "\n"
        return text


if __name__ == "__main__":
    main()

