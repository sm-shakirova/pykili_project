# pykili_project

### Описание ###

Лингвистическое исследование на основе собранного вручную корпуса

### План проекта ###

1. Сбор данных: 
    - чаты мессенджеров 
        - проблема: авторское право, конфиденциальность личных данных
    - книги в эпистолярном жанре

2. Обработка данных, извлечение текстов:
    - книги в формате txt
    - телеграм чаты в формате json
    - ВК чаты в формате html
        - проблема: баг с вычленением года отправки сообщения (проблема в регулярке)
        - решение: постараюсь протестировать другие регулярки для поиска кода на каждом отдельном файле, делать сет из списка найденных годов

3. Морфопарсер
5. Лингвистическое исследование:
    - Анализ сочетаемости прилагательных с существительными
        - проблема: сложность с обработкой большого количества данных
        - решение: разбиение на части, дополнительный код, соединяющий части вместе
    - Подсчет количества частей речи по годам в процентах
    - Список частотных слов по годам
7. Создание графиков на основе полученных данных

### Используемые модули ###

- os
- re
- json
- string
- collections
- pymorphy

### Участники ###

- Софья Шакирова, БКЛ-202
- Полина Карпова, БКЛ-204
- Татьяна Ковтун, БКЛ-204
