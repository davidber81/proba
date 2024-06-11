# import parser_2gis
#
# parser-2gis -i "https://2gis.ru/moscow/search/тату-салоны"  -o "C:\results.csv" -f csv
#
# -i "https://2gis.ru/rostov/search/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B8/rubricId/207"
#
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# url = ["https://habr.com/ru/post/580888"]
#
# file = open('text.txt', 'a')
#
# for x in url:
#     html_code = str(urlopen(x).read(), 'utf-8')
#     soup = BeautifulSoup(html_code, 'html.parser')
#
#     s = soup.find('title').text
#     file.write(s + '\n')
#     p = soup.find_all('p')
#     for i in p:
#         print(i.text)
#         file.write(i.text + '\n')



import CSV
import JSON
import ОС
import систему
import TemporaryDirectory

import pytest
from parser_2gis import parser_main


def  check_csv_result (result_path , num_records):
    """Проверьте вывод CSV.
    Аргументы:
        file_path: Путь к таблице CSV.
        num_records: Ожидаемое количество записей.
    """
    with open (result_path, 'r', code = 'utf-8-sig' , errors = 'replace') как  f :
        читатель  =  csv . читатель ( ж )
        Assert  len ​​( list ( reader )) ==  num_records  +  1   # `num_records` + заголовок


def  check_json_result ( result_path , num_records ):
    """Проверьте вывод JSON.
    Аргументы:
        file_path: Путь к файлу JSON.
        num_records: Ожидаемое количество записей.
    """
    с  open ( result_path , 'r' , кодирование = 'utf-8-sig' , ошибки = 'replace' ) как  f :
        документ  =  JSON . нагрузка ( ф )
        утверждать  len ( doc ) ==  num_records


тестовые данные  = [
    [ 'csv' , check_csv_result ],
    [ 'json' , check_json_result ],
]


@pytest .​ отметка . параметризовать ( 'формат, result_checker' , тестовые данные )
def  test_parser ( monkeypatch , format , result_checker , num_records = 5 ):
    """Проанализируйте записи TOP `num_records` и проверьте файл результатов.
    Аргументы:
        формат: формат результата (csv или json).
        result_checker: Функция, которая проверяет результат анализа.
        num_records: количество записей для анализа.
    """
    с  обезьянкой . context () как  m , TemporaryDirectory () как  tmpdir :
        result_path  =  ОС . путь . присоединиться ( tmpdir , f'output. { format } ' )

        м . setattr ( sys , 'argv' , [
            Операционные системы . путь . абспут ( __file__ ),
            '-i' , 'https://2gis.ru/moscow/search/Аптеки' ,
            '-o' , путь_результата ,
            '-f' , формат ,
            '--parser.max-records' , f' { num_records } ' ,
            '--chrome.headless' , 'да' ,
        ])

        # Запускаем парсер по популярному запросу
        # который должен иметь как минимум `num_records` записей.
        парсер_мейн ()

        # Проверяем результаты анализа
        result_checker ( result_path , num_records )