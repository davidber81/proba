def is_prime(func):
    def wrapper (*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:
            text = 'Составное'
        else:
            text = 'Простое'

        print(text)
        return result
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c
x = sum_three(2, 3, 6)
print(x)