def create_operation(operation):
    if operation == "multi":
        def multi(x, y):
            return x * y
        return multi
    elif operation == "divis":
        def divis(x, y):
            return x / y
        return divis
my_func_multi = create_operation("multi")
print(my_func_multi(1,2))
my_func_divis = create_operation("divis")
print(my_func_divis(1,2))


multiply = lambda x: x ** 2
print(multiply(2))
def multiply_def(x):
   return x ** 2
print(multiply_def(2))

class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
       print(f'Вызываемые объекты: \nСтороны: {a}, {b}')
   def __call__(self):
       return self.a * self.b
repeat = Rect(2, 4)
print(f'Площадь:', repeat())