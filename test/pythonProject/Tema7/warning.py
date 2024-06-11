import warnings
a = float(input())
b = float(input())

def fun_with_warning(a, b):
        try:
            if b <= 0.01:
                warnings.warn('Это важное предупреждение', category=ZeroDivisionError)
            print(f'Деление: {a} / {b} = {a / b}')
        except ZeroDivisionError:
            print('Предупреждение было перехваченно как исключение:')

print("Пример 1: Фильтр 'error'")
warnings.simplefilter("error", ZeroDivisionError)
fun_with_warning(a, b)
print("\n")

print("Пример 2: Фильтр 'always'")
warnings.simplefilter("always", ZeroDivisionError)
fun_with_warning(a, b)
print("\n")

print("Пример 3: Фильтр 'ignore'")
warnings.simplefilter("ignore", ZeroDivisionError)
fun_with_warning(a, b)
print("\n")