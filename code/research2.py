from collections import defaultdict
import json
import os


def count_pos(file):
    """Функция для сортировки частей речи по годам"""
    with open(file, 'r', encoding='utf-8') as f:
        lst = json.load(f)
    tags = ['NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB', 'INFN',
            'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO',
            'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'ALL']  # тэги из документации pymorphy
    dct = defaultdict(dict)
    for word in lst:
        if word['year'] not in dct[word['POS']]:
            dct[word['POS']][word['year']] = 0
        dct[word['POS']][word['year']] += 1
        if word['year'] not in dct['ALL']:
            dct['ALL'][word['year']] = 0
        dct['ALL'][word['year']] += 1
    return dct


def find_percent(dct):
    """Считает относительную частотность частей речи в процентах для каждого года"""
    main_dict = {}
    for pos, inner_dict in dct.items():
        new_list = []
        for year, value in inner_dict.items():
            percent = (value / dct['ALL'][year]) * 100
            new_dict = {'year': year, 'variable': round(percent, 2)}
            new_list.append(new_dict)
        main_dict[pos] = new_list
    main_dict.pop('ALL')
    return main_dict


if __name__ == "__main__":
    path = input('Путь к папке со всеми файлами с разметкой: ')
    main_dict = {}
    for dirs, folder, files in os.walk(path):
        for file in files:
            result = count_pos(file)
            for year, inner_dict in result.items():
                if year not in main_dict:
                    main_dict[year] = {}
                for pos, value in inner_dict.items():
                    main_dict[year][pos] += value
    with open(input('Назвать файл с результатами по частям речи: '), 'w', encoding='utf-8') as new_file:
        json.dump(find_percent(main_dict), new_file, ensure_ascii=False, indent=1)
