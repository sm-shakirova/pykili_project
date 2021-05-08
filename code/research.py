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
                if noun_ind - ind in (1, 2) \
                        and word['case'] == lst[noun_ind]['case'] \
                        and word['number'] == lst[noun_ind]['number'] \
                        and word['gender'] == lst[noun_ind]['gender']:
                    if 2010 in dct:
                        if lst[noun_ind]['lemma'] in dct[2010]:
                            dct[2010][lst[noun_ind]['lemma']].append(word['lemma'])
                        else:
                            dct[2010][lst[noun_ind]['lemma']] = [word['lemma']]
                    else:
                        dct[2010] = {lst[noun_ind]['lemma']: [word['lemma']]}
                elif noun_ind - ind in (-1, -2) \
                        and word['case'] == lst[noun_ind]['case'] \
                        and word['number'] == lst[noun_ind]['number'] \
                        and word['gender'] == lst[noun_ind]['gender']:
                    if 2010 in dct:
                        if lst[noun_ind]['lemma'] in dct[2010]:
                            dct[2010][lst[noun_ind]['lemma']].append(word['lemma'])
                        else:
                            dct[2010][lst[noun_ind]['lemma']] = [word['lemma']]
                    else:
                        dct[2010] = {lst[noun_ind]['lemma']: [word['lemma']]}
    for year, inner_dct in dct.items():
        for noun, adj in inner_dct.items():
            inner_dct[noun] = list(set(adj))  # нужно отсортировать еще и по количеству
    return dct


if __name__ == "__main__":
    with open(input('Путь к папке с разметкой: '), 'r', encoding='utf-8') as file:
        data = json.load(file)
    result = sort_words(data)
    
