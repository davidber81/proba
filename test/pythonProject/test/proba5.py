def values_list(number, russian, english, number1, russian1, english1):
    print("Число -", number)
    print("Русский -", russian)
    print("Английский -", english)
    print("Получается :", number, russian, english)
    print("Число -", number1)
    print("Русский -", russian1)
    print("Английский -", english1)
    print("Получается :", number1, russian1, english1)
    print("Получается всего :", number, russian, english, number1, russian1, english1)

values_dict=[1, 'строка', 'True']
print_params={'number1':2, 'russian1':'слово', 'english1':'Module'}
values_list(*values_dict, **print_params)




