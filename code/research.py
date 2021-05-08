import json


def sort_words(lst):
    noun_indexes = []
    for ind, word in enumerate(lst):
        if word['POS'] == 'NOUN':
            noun_indexes.append(ind)
    dct = {}
    for ind, word in enumerate(lst):
        if word['POS'] == 'ADJF':
            for noun_ind in noun_indexes:
                if noun_ind - ind in (1, 2):
                    noun = lst[noun_ind]
                elif noun_ind - ind == -1:
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
    for year, inner_dct in dct.items():
        for noun, adj in inner_dct.items():
            inner_dct[noun] = list(set(adj))  # нужно отсортировать еще и по количеству
    return dct


if __name__ == "__main__":
    with open(input('Путь к папке с разметкой: '), 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(sort_words(data), new_file, ensure_ascii=False, indent=1)
