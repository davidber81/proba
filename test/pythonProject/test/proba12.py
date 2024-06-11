def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1=factorial(n=n-1)
    return n*factorial_n_minus_1
print(factorial(27))


def test_them_all(*args, **kwargs):
    print('test_them_all')
    print('тип args:', type(args))
    print(args)
    for i, args in enumerate(args):
        print('позиционный параметр:', i, args)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именнованыый аргумент:', key, '=', value)

test_them_all('Дима', 'Rostov', 42, name='Коля', address='Pekin')
