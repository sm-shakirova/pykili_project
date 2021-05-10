import json


def sort_pos(lst):
    """Функция для сортировки частей речи по годам"""
    tags = ['NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB', 'INFN',
           'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO',
           'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'ALL']  # можно еще соеденить например ADJF и ADJS, но не знаю нужно ли
    main_dct = {}
    for word in lst:
        if word['year'] not in main_dct:
            main_dct[word['year']] = dict.fromkeys(tags, 0)
        main_dct[word['year']]['ALL'] += 1
        if word['POS'] in tags:
            main_dct[word['year']][word['POS']] += 1
    #  for key, val in main_dct.items():
        #  print(key, val)
    return main_dct


if __name__ == "__main__":
    with open(input('Путь к файлу с разметкой: '), 'r', encoding='utf-8') as file:
        data = json.load(file)
    sort_pos(data)
    """with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(sort_words(data), new_file, ensure_ascii=False, indent=1)"""


