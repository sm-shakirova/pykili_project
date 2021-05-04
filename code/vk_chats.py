import os
import re
import json


def get_messages(file_path):
    with open(file_path, 'r', encoding='Windows-1251') as file:
        data = file.read()
    for smile in set(re.findall(r'\d*;?&#\d*;?', data)):  # удаляет смайлики
        data = data.replace(smile, '')
    for link in set(re.findall(r'http\S+', data)):  # удаляет ссылки
        data = data.replace(link, '')
    messages = re.findall(r'(?<=<div>).+?(?=<div class="kludges">)', data)  # находит тексты сообщений
    for ind, message in enumerate(messages):
        messages[ind] = message.replace('<br>', '').replace('&quot;', '')
    return messages


if __name__ == "__main__":
    path = input('Путь к папке с сообщениями из VK на вашем компьютере: ')
    all_texts = []
    for dirs, folder, files in os.walk(path):  
        # еще есть listdir, но он проходится только по поверхности
        # документация по walk: https://docs.python.org/3/library/os.html#os.walk
        # рекурсивная штука, поэтому находит все файлы, в том числе во внутренних папках
        for file in files:
            texts = get_messages(os.path.join(dirs, file))
            all_texts.extend(texts)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(all_texts, new_file, ensure_ascii=False, indent=2)
