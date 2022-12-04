import re
from os.path import exists
from hazm import *
import requests

if not exists("unique-words.txt"):
    open("unique-words.txt", 'a').close()

urls = [
# "https://huggingface.co/datasets/SLPL/naab/resolve/main/data/test-00000-of-00003.txt"
# "https://raw.githubusercontent.com/milad-4274/persian_news/master/main_news.csv"
"https://storage.googleapis.com/danielk-files/farsi-text/merged_files/fawiki_merged.txt"
]

for url in urls:
    text = requests.get(url).text

    text = Normalizer().normalize(text)
    text = re.sub(r'[^آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ]', ' ', text)
    words = list(set(WordTokenizer().tokenize(text)))

    existing_words = open('unique-words.txt', "r",
                          encoding="utf-8").read().splitlines()

    existing_words = list(filter(None, existing_words))
    combine_list = list(set(words + existing_words))

    with open('unique-words.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(combine_list))
