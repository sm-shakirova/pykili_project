import json


def count_pos(file):
    """Функция для сортировки частей речи по годам"""
    with open(file, 'r', encoding='utf-8') as f:
        lst = json.load(f)
    tags = ['NOUN', 'ADJ', 'VERB', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO',
            'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'ALL', 'UNKN']  # немного обобщенные тэги из документации pymorphy
    dct = {}
    for tag in tags:
        dct[tag] = {}
    for word in lst:
        if word['POS'] in ('ADJF', 'ADJS', 'COMP'):
            if word['year'] not in dct['ADJ']:
                dct['ADJ'][word['year']] = 0
            dct['ADJ'][word['year']] += 1
        elif word['POS'] in ('VERB', 'INFN'):
            if word['year'] not in dct['VERB']:
                dct['VERB'][word['year']] = 0
            dct['VERB'][word['year']] += 1
        elif word['POS'] == 'None':
            if word['year'] not in dct['UNKN']:
                dct['UNKN'][word['year']] = 0
            dct['UNKN'][word['year']] += 1
        elif word['POS'] in ('NOUN', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB',
                             'NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ'):
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
    main_dict = count_pos(input('Название файла: '))
    with open(input('Назвать файл с результатами по частям речи: '), 'w', encoding='utf-8') as new_file:
        json.dump(find_percent(main_dict), new_file, ensure_ascii=False, indent=1)
