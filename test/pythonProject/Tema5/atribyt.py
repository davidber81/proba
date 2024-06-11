class House:
    def __init__(self):
        self.numberOfFloors = 10

house = House()

for i in range(1, house.numberOfFloors+1):
    print("Текущий этаж равен", i)


