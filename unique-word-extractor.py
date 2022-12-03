import re
from os.path import exists
from hazm import *

if not exists("unique-words.txt"):
    open("unique-words.txt", 'a').close()

# Cleaning
text = open('input.txt', 'r', encoding='utf-8').read()
text = Normalizer().normalize(text)
text = re.sub(r'[^آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ]', ' ', text)
words = list(set(WordTokenizer().tokenize(text)))

existing_words = open('unique-words.txt', "r",
                      encoding="utf-8").read().splitlines()

existing_words = list(filter(None, existing_words))
combine_list = list(set(words + existing_words))


with open('unique-words.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(combine_list))
