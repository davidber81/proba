my_spisok = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

you_spisok = [1, 25, 49, 121, 1225, 7921]

result1 = map(lambda x: x**2, filter(lambda x: x%2, my_spisok))
print(list(result1))
result2 = map(lambda y: y**2, filter(lambda y: y%2, you_spisok))
print(list(result2))