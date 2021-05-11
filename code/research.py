import json


def sort_words(lst):
    """Функция для сортировки сочетаний прилагательных с существительными по годам"""
    noun_indexes = []
    for ind, word in enumerate(lst):
        if word['POS'] == 'NOUN':
            noun_indexes.append(ind)
    dct = {}
    for ind, word in enumerate(lst):  # NB! сортирует долго
        if word['POS'] == 'ADJF':
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
    for year, inner_dict in dct.items():
        for noun, inner_list in inner_dict.items():
            adj_dict = dict.fromkeys(set(inner_list))
            for adj in adj_dict:
                adj_dict[adj] = inner_list.count(adj)
            adj_dict = sorted(adj_dict, key=adj_dict.get, reverse=True)  # сортировка по частотности
            inner_dict[noun] = [key for key in adj_dict]
    return dct


if __name__ == "__main__":
    with open(input('Путь к папке с разметкой: '), 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(sort_words(data), new_file, ensure_ascii=False, indent=1)
