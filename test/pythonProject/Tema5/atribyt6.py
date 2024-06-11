class Vehicle:
    vehicle_type = "none"
class Car:
    price = 1000000
    def horse_powers(self):
        return 200
class Nissan(Vehicle, Car):
    price = 555555
    vehicle_type = "two"
    def horse_powers(self):
        return 120
my_car = Nissan()
vehicle = my_car.vehicle_type
price = my_car.price
print(vehicle)
print(price)

