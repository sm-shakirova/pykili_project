# pykili_project

### Описание ###

Лингвистическое исследование на основе собранного вручную корпуса

### Текущие задачи ###

+ распарсить данные
- прогрузить данные через research.py
- поправить баг в скрипте по частям речи
- выводы по исследованию
- сделать презентацию

### План проекта ###

1. Собрать данные, опросить знакомых, обкачать паблики: 
    - чаты мессенджеров 
        - проблема: авторское право, конфиденциальность личных данных
    - книги в эпистолярном жанре

2. Написать код дбработки данных, конкретно для извлечения текстов и извлечения годов:
    - книги в формате txt
    - телеграм чаты в формате json
    - ВК чаты в формате html
        - проблема: ну знаете регулрку напишешь, а потом окажется, что все равно нашел не все, поэтому регулярки совершенствовались по мере нахождения новых штук
3. Морфопарсер, написать код, создающий список слов с морфологическим разбором (начальной формой, частью речи, некоторыми грамматическими категориями, имеющими значениями для именных категорий, т.е. существительных и прилагательных: падеж, число, род)
    - проблема: опечатки, несуществующие слова, сленг (например, "лол кек" вообще непонятно как парсить)
    - решение: если останутся время силы, можно сделать базу данных наиболее популярных штук, которые нельзя распарсить стандартным парсером, например регулярками находить все варианты "ахахах" в том числе с опечатками и записывать в смех или "пфф" или те же "лол кек"
4. Лингвистическое исследование, написать несколько алгоритмов сортировки распарсенных данных:
    - Анализ сочетаемости прилагательных с существительными
        - проблема: сложность с обработкой большого количества данных
        - решение: разбиение на части, дополнительный код, соединяющий части вместе
        - проблема: хотя наш алгоритм действительно находит большинство прилагательных к существительным, свободный порядок слов в русском языке мешает найти все случаи
    - Подсчет количества частей речи по годам в процентах
        - проблема: баг с вычленением года отправки сообщения, я думала проблема в регулярке, но оказалось, что где-то вдругом месте
    - Список частотных слов по годам
5. Создание графиков на основе полученных данных

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
