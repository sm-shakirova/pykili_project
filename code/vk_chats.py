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
    messages = re.findall(r'(?<=<div class="message__header">).+?\n.+?(?=<div class="kludges">)', data)
    for ind, message in enumerate(messages):
        year = re.search(r'\d{4}', message)[0]  # находит год
        message = re.search(r'(?<=<div>).*', message)[0]  # вычленяет текст сообщения
        message = message.replace('<br>', '').replace('&quot;', '')
        if message != '':
            messages[ind] = [year, message]
    return messages


if __name__ == "__main__":
    path = input('Путь к папке messages: ')
    text = []
    for dirs, folder, files in os.walk(path):
        for file in files:
            messages = get_messages(os.path.join(dirs, file))
            text.extend(messages)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(text, new_file, ensure_ascii=False, indent=2)
        
