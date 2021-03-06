import json
import os


def connect_adjectives(dirs, files):
    main_dict = {}
    for file in files:
        with open(os.path.join(dirs, file), 'r', encoding='utf-8') as f: 
            dct = json.load(f)
        for year, inner_dict in dct.items():
            if year not in main_dict:
                main_dict[year] = {}
            for noun, inner_list in inner_dict.items():  # добавляет данные отдельных файлов в один большой словарь main_dict
                if noun not in main_dict[year]:
                    main_dict[year][noun] = []
                main_dict[year][noun].extend(inner_list)
    return main_dict


def connect_parsed(dirs, files):
    main_list = None
    for file in files:
        with open(os.path.join(dirs, file), 'r', encoding='utf-8') as f:
            data = json.load(f)
        if main_list is None:
            main_list = data
        else:
            main_list.extend(data)  # добавляет списки слов с разметкой в один большой список main_list
    return main_list


if __name__ == '__main__':
    path = input('Путь к папке с файлами: ')
    for dirs, folder, files in os.walk(path):  # проходится по папкам
        
        # NB! если нужно соединить результат работы research_1.py в названии папки должно быть слово "adjectives"
        if 'adjectives' in dirs:
            with open(input('Назвать файл с результатами по прилагательным: '), 'w', encoding='utf-8') as new_file:
                json.dump(connect_adjectives(dirs, files), new_file, ensure_ascii=False, indent=1)
        
        # NB! если нужно соединить результат работы parser.py в названии папки должно быть слово "parsed"
        elif 'parsed' in dirs:  
            with open(input('Назвать файл с объединенными распарсенными файлами: '), 'w', encoding='utf-8') as new_file:
                json.dump(connect_parsed(dirs, files), new_file, ensure_ascii=False, indent=1)
