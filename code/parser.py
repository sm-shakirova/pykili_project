from pymorphy2 import MorphAnalyzer
from string import punctuation
import json


def parse_text(data):
    """Функция принимает список текстов с годами их написания и делает разбор каждого слова"""
    result = []
    morph = MorphAnalyzer()
    if isinstance(data[0], list):
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
    else:
        text = [word.lower().strip(punctuation) for word in data[1].split()]
        text = [word for word in text if word != '']
        for word in text:
            parser = morph.parse(word)[0]
            dct = {
                    'year': data[0],
                    'word': str(parser.word),
                    'lemma': str(parser.normal_form),
                    'POS': str(parser.tag.POS),
                    'case': str(parser.tag.case),
                    'number': str(parser.tag.number),
                    'gender': str(parser.tag.gender)
            }
            result.append(dct)
    return result


if __name__ == "__main__":
    with open(input('Путь к файлу с текстами (и годами): '), 'r', encoding='utf-8') as file:
        messages = json.load(file)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(parse_text(messages), new_file, ensure_ascii=False, indent=1)
