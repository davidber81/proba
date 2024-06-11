# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#
#     num = num // 10
#
# print(total)

import requests
from urllib.request import urlopen
# from extractor import LinkExtractor
# from utils import time_track
from html.parser import HTMLParser
from html.entities import name2codepoint

# Для открытия сайта нажимаем прав.кноп.м. или ctrl + U
# Далее инструмент разработки
# чтобы его открыть кликните правой кнопкой мыши по сайту и просмотреть код
# Из библиотеки нам требуется загрузить html, далее слегка его распарсить (html.parser),
# найти ссылку на src на джава скрипт, высунать файл и посмотреть что будет.
# html.parser - открыли приложение, скопировали, и вложили здесь,
# Удаляем всё лишнее (всю нижнюю часть)
# Далее

sites = [
    'https://www.kinopoisk.ru/',   # нажим.колёсиком по ссылке, идёт переброс на сайт
    'https://www.youtube.com/',
    'https://urban-university.ru/',
    'https://www.ivi.ru/',
    'https://ya.ru',
    'https://www.google.ru/?hl=ru',
]


class MyHTMLParser(HTMLParser):
    # handle_starttag - ф-ция обработки, означ.парсинг нашёл в нашем файле теги с их атрибутами
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("attr:", attr)


for url in sites:
    res = urlopen(url)   # долеенам надо получить с него данные urlopen - она открывает
    html_data = res.read()
    # html_data = html_data.decode('utf-8')   # файл должен быть в кодировке
    total_bytes = len(html_data)    # total_bytes=0, т.е. длинне html_data, таким образом мы посчитали размер
    parser = MyHTMLParser
    parser.feed(html_data)   # вложим в парсинг информацию например html_data