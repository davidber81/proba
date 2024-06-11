class Car:
    price = 1000000
    def __init__(self, model):
        self.model = model
    def horse_powers(self):
        return 200

    def __str__(self):
        return '{} модель {} цена {} мощность'.format(self.__class__.__name__, self.price, self.horse_powers())


class Nissan(Car):
    price = 500000
    def horse_powers(self):
        return 150
class Kia(Car):
    price = 300000
    def horse_powers(self):
        return 130

my_car = Nissan('model')
print(my_car)

my_car2 = Kia('model')
print(my_car2)



# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите функцию horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price, а также переопределите функцию horse_powers