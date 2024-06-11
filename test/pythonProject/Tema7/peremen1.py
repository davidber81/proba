# from pprint import pprint

file_name = 'stix1.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line)

print(file.closed)



# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with
# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# Получившийся код прикрепите к заданию текстом