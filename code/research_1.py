import json


def extract_adjectives(lst):
    """Функция для сортировки сочетаний прилагательных с существительными по годам"""
    noun_indexes = []
    for ind, word in enumerate(lst):
        if word['POS'] == 'NOUN':
            noun_indexes.append(ind)
    dct = {}
    for ind, word in enumerate(lst):
        if word['POS'] == 'ADJF':
            noun = False
            for noun_ind in noun_indexes:
                if noun_ind - ind == 1:
                    noun = lst[noun_ind]
                elif noun_ind - ind == 2:
                    noun = lst[noun_ind]
            if noun \
                    and word['year'] == noun['year'] \
                    and word['case'] == noun['case'] \
                    and word['number'] == noun['number'] \
                    and word['gender'] == noun['gender']:
                if word['year'] in dct:
                    if noun['lemma'] in dct[word['year']]:
                        dct[word['year']][noun['lemma']].append(word['lemma'])
                    else:
                        dct[word['year']][noun['lemma']] = [word['lemma']]
                else:
                    dct[word['year']] = {noun['lemma']: [word['lemma']]}
    return dct


def sort_adjectives(dct):
    """Сортирует прилагательные по частотности"""
    for year, inner_dict in dct.items():
        for noun, inner_list in inner_dict.items():
            adj_dict = dict.fromkeys(set(inner_list))
            for adj in adj_dict:
                adj_dict[adj] = inner_list.count(adj)
            adj_dict = sorted(adj_dict, key=adj_dict.get, reverse=True)
            inner_dict[noun] = [key for key in adj_dict]
        dct[year] = inner_dict
    return dct


if __name__ == "__main__":
    with open(input('Название файла: '), 'r', encoding='utf-8') as f:
        lst = json.load(f)
    dct = extract_adjectives(lst)
    with open(input('Назвать файл с результатами по прилагательным: '), 'w', encoding='utf-8') as new_file:
        json.dump(sort_adjectives(dct), new_file, ensure_ascii=False, indent=1)
