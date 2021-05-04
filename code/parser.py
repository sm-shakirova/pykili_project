from pymorphy2 import MorphAnalyzer
from string import punctuation
import json


def parse_text(data):
    text = ' '.join(data)
    text = [word.lower().strip(punctuation) for word in text.split()]
    text = [word for word in text if word != '']
    result = []
    morph = MorphAnalyzer()
    for word in text:
        parser = morph.parse(word)[0]
        dct = {'word': str(parser.word), 'lemma': str(parser.normal_form), 'tag': str(parser.tag)}
        result.append(dct)
    return result


if __name__ == "__main__":
    with open(input('Путь к файлу с текстом: '), 'r', encoding='utf-8') as file:
        messages = json.load(file)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(parse_text(messages), new_file, ensure_ascii=False, indent=2)
