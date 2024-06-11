from pprint import pprint

file_name = 'stix.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)


# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль
# Закройте файл