from pymorphy2 import MorphAnalyzer
from string import punctuation
import json


def parse_text(data):
    result = []
    morph = MorphAnalyzer()  # NB! долго парсит большие файлы 
    for el in data:
        text = [word.lower().strip(punctuation) for word in el[1].split()]
        text = [word for word in text if word != '']
        for word in text:
            parser = morph.parse(word)[0]
            dct = {
                    'year': el[0],
                    'word': str(parser.word),
                    'lemma': str(parser.normal_form),
                    'POS': str(parser.tag.POS),
                    'case': str(parser.tag.case),
                    'number': str(parser.tag.number),
                    'gender': str(parser.tag.gender)
            }
            # список тэгов: https://pymorphy2.readthedocs.io/en/latest/user/grammemes.html
            result.append(dct)
    return result


if __name__ == "__main__":
    with open(input('Путь к файлу с вычлененными текстами: '), 'r', encoding='utf-8') as file:
        messages = json.load(file)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(parse_text(messages), new_file, ensure_ascii=False, indent=1)
