import os
import re
import json


def vk_messages(file_path):
    """Функция для извлечения сообщений и годов их отправки из чатов ВК"""
    with open(file_path, 'r', encoding='Windows-1251') as file:
        data = file.read()
    for smile in set(re.findall(r'\d*;?&#\d*;?', data)):  # удаляет смайлики
        data = data.replace(smile, '')
    for link in set(re.findall(r'http\S+', data)):  # удаляет ссылки
        data = data.replace(link, '')
    messages = re.findall(r'(?<=<div class="message__header">).+?\n.+?(?=<div class="kludges">)', data)
    for ind, message in enumerate(messages):
        year = re.search(r'\d{4}', message)[0]  # находит год
        message = re.search(r'(?<=<div>).*', message)[0]  # текст сообщения
        message = message.replace('<br>', '').replace('&quot;', '')
        if message != '':
            messages[ind] = [year, message]
    return messages


def tg_messages(file_path):
    """Функция для извлечения сообщений и годов их отправки из чатов Телеграм"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    messages = []
    try:
        for i in data['chats']['list']:
            for j in i['messages']:
                year = re.search(r'\d{4}', j['date'])[0]
                text = j['text']
                if type(text) == str and text != '':
                    messages.append([year, text])
    except KeyError:
        for j in data['messages']:
            year = re.search(r'\d{4}', j['date'])[0]
            text = j['text']
            if type(text) == str and text != '':
                messages.append([year, text])
    return messages


def txt_books(file_path):
    """Функция для извлечения годов написания и самих текстов из книг"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    year = re.search(r'\d{4}', data)[0]
    text = data.lstrip(year)
    return [year, text]


if __name__ == "__main__":
    path = input('Путь к папке (не файлу): ')
    data = []
    for dirs, folder, files in os.walk(path):
        for file in files:
            name, extension = os.path.splitext(file)
            if extension == '.html':
                texts = vk_messages(os.path.join(dirs, file))
            elif extension == '.json':
                texts = tg_messages(os.path.join(dirs, file))
            elif extension == '.txt':
                texts = txt_books(os.path.join(dirs, file))
            data.extend(texts)
    with open(input('Назвать новый файл: '), 'w', encoding='utf-8') as new_file:
        json.dump(data, new_file, ensure_ascii=False, indent=1)
