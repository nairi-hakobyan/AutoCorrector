from collections import Counter
from nltk import edit_distance
import re
from utils.preprocessing import get_words
import numpy as np


print(np.array([1,2,3]))
class AutoCorrect:
    def __init__(self, window_size=0, real_time=True):
        self.vocabulary = None
        self.window_size = window_size
        self.real_time = real_time
        self.dictionary = dict()

    def set_dict(self, text):
        self.vocabulary = set(text)
        text = [tuple(text[i:i + self.window_size + 1]) for i in range(len(text) - self.window_size)]
        self.dictionary = Counter(text)

    def correct_word(self, word, prev_words=()):
        min_dist = edit_distance(word, list(self.dictionary.keys())[0])
        closest_word = list(self.dictionary.keys())[0][-1]
        for possible_word in self.vocabulary:
            new_dist = edit_distance(word, possible_word)
            if new_dist == min_dist:
                if self.dictionary[prev_words + (possible_word,)] > self.dictionary[prev_words + (closest_word,)]:
                    closest_word = possible_word
            elif new_dist < min_dist:
                closest_word = possible_word
                min_dist = new_dist

        return closest_word

    def correct_sentence(self, text):
        text_split = re.sub(r'[^\w]', ' ', text).split()
        for i, word in enumerate(text_split):
            if word not in self.dictionary:
                text = text.replace(word,
                                    self.correct_word(word, prev_words=tuple(text_split[i - self.window_size:i])))

        return text

words = get_words()
autocorrector = AutoCorrect(window_size=1)
autocorrector.set_dict(words)
print(autocorrector.correct_sentence('hello, my adress is unknoun'))
