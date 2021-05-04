from pymorphy2 import MorphAnalyzer
from string import punctuation
import json


def parse_text(data):
    if isinstance(data, list):
        data = ' '.join(data)
    text = [word.lower().strip(punctuation) for word in data.split()]
    text = [word for word in text if word != '']
    result = []
    morph = MorphAnalyzer()  # NB! большой файл может грузить несоклько минут
    for word in text:
        parser = morph.parse(word)[0]
        dct = {
                  'word': str(parser.word),
                  'lemma': str(parser.normal_form),
                  'POS': str(parser.tag.POS),
        }
        tags = str(parser.tag).replace(f'{str(parser.tag.POS)},', '')
        if tags == str(parser.tag.POS):
            dct['tags'] = None
        elif tags != '':
            dct['tags'] = tags
        # список тэгов: https://pymorphy2.readthedocs.io/en/latest/user/grammemes.html
        result.append(dct)
    return result


if __name__ == "__main__":
    with open(input('Путь к файлу с текстом: '), 'r', encoding='utf-8') as file:
        messages = json.load(file)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(parse_text(messages), new_file, ensure_ascii=False, indent=2)
