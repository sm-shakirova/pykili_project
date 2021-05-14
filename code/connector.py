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
            for noun, inner_list in inner_dict.items():
                if noun not in main_dict[year]:
                    main_dict[year][noun] = []
                main_dict[year][noun].extend(inner_list)
    return main_dict


def connect_pos(dirs, files):
    main_dict = None
    for file in files:
        with open(os.path.join(dirs, file), 'r', encoding='utf-8') as f:
            dct = json.load(f)
        for pos, inner_dict in dct.items():
            if not main_dict:
                main_dict = dct
            else:
                for year, value in inner_dict.items():
                    main_dict[pos][year] += value
    return main_dict


def connect():
    pass


if __name__ == '__main__':
    path = input('Путь к папке с файлами: ')
    for dirs, folder, files in os.walk(path):
        if 'adjectives' in dirs:
            with open(input('Назвать файл с результатами по прилагательным: '), 'w', encoding='utf-8') as new_file:
                json.dump(connect_adjectives(dirs, files), new_file, ensure_ascii=False, indent=1)
        elif 'pos' in dirs:
            with open(input('Назвать файл с результатами по частям речи: '), 'w', encoding='utf-8') as new_file:
                json.dump(connect_pos(dirs, files), new_file, ensure_ascii=False, indent=1)
