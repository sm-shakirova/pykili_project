import os
import re
import json


def get_messages(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        data = file.read()
    messages = re.findall(r'(?<=<div>).+?(?=<div class="kludges">)', data)
    return messages


if __name__ == "__main__":
    path = input('Путь до папки с сообщениями из VK на вашем компьютере: ')
    all_texts = []
    for dirs, folder, files in os.walk(path):  # еще есть listdir, но он проходится только по поверхности
        # документация по walk: https://docs.python.org/3/library/os.html#os.walk
        # рекурсивная штука, поэтому находит все файлы, в том числе во внутренних папках
        for file in files:
            texts = get_messages(os.path.join(dirs, file))
            all_texts.extend(texts)
    with open('messages.json', 'w', encoding='utf-8') as new_file:
        json.dump(all_texts, new_file, ensure_ascii=False, indent=2)
