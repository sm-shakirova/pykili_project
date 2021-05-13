import re
import string
import json
from operator import itemgetter


frequency = {}
with open(input('Название файла с леммами: '), 'r') as text_file:
    text_str = text_file.read().lower()
    q_pattern = re.findall(r'"lemma": "([\s\S]+?)",', text_str)

    for word in q_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    my_dict = {}
    for words in frequency_list:
        my_dict[words] = [frequency[words]]

    sorted_dict = sorted(my_dict.items(), key=itemgetter(1), reverse=True)

    with open("freqfreqlist.json", "a", encoding="utf-8") as f:
        json.dump(sorted_dict, f, ensure_ascii=False, indent=1)
