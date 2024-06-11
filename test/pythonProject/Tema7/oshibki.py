s = input()
def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print(f'Ошибка: невозможно преобразовать {s} в целое число')
string_to_int(s)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Ошибка: файл {filename} не найден')
    except IOError as filename:
        print(f'Ошибка ввода/вывода при работе с файлом {filename}.')
read_file(filename='r')


a = input()
b = input()
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Ошибка: деление на ноль.')
    except TypeError:
        print('Ошибка: аргументы должны быть числами.')
divide_numbers(a, b)


index = input()
lst = input()
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        print(f'Ошибка: индекса {index} вне диапазона списка')
    except TypeError:
        print('Ошибка: индекс должен быть целым числом.')
access_list_element(lst=66, index=55)

