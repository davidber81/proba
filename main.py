class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Sclad:
    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.set_road_out = None
        self.queue_in = []
        self.queue_out = []
    def __str__(self):
        return 'Склад {} груза {}'.format(self.name, self.content)
    def set_road_out_1(self, road):
        self.set_road_out = road
    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print('{} прибыл грузовик {}'.format(self.name, truck))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print('{} грузовик готов {}'.format(self.name, truck))
    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)

class Mashini:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} топлива {}'.format(self.model, self.fuel)
    def tank_up(self):
        self.fuel += 1000
        Mashini.total_fuel += 1000
        print('{} заправился'.format(self.model))

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True

class Truck(Mashini):
    fuel_rate = 50
    dead_time = 0
    def __init__(self, model, body_space=0):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0
    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.cargo)

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print('{} выехал в путь'.format(self.model))
    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print('{} едет по дороге, осталось {}'.format(self.model, self.distance_to_target))
        else:
            self.place = self.place.end
            self.place.truck_arrived(self)
            print('{} доехал'.format(self.model))

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1

class Pogruzchik(Mashini):
    fuel_rate = 30


    def __init__(self, model, bucket_capacity, sclad=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.sclad = sclad
        self.role = role
        self.cargo = 0
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.cargo)

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.sclad.get_next_truck()
                print('{} взял в работу {}'.format(self.model, self.truck))
            elif self.role == 'loader':
                self.load()
            else:
                self.unload()
            if self.truck is None:
                Truck.dead_time += 1


    def load(self):
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.sclad.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.sclad.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest
        print('{} грузил {}'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.sclad.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.sclad.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.sclad.content -= self.truck.cargo
            self.truck.cargo += self.truck.cargo
        print('{} выгружал {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.sclad.track_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000

msc = Sclad(name='Москва', content=TOTAL_CARGO)
spb = Sclad(name='Питер', content=0)

msc_spb = Road(start=msc, end=spb, distance=715)
spb_msc = Road(start=spb, end=msc, distance=780)

msc.set_road_out_1(msc_spb)
spb.set_road_out_1(spb_msc)

loader1 = Pogruzchik(model='Bobcat', bucket_capacity=1000, sclad=msc, role='loader')
loader2 = Pogruzchik(model='Lonking', bucket_capacity=500, sclad=spb, role='unloader')

truck1 = Truck(model='Камаз', body_space=5000)
truck2 = Truck(model='Кам', body_space=2000)

msc.truck_arrived(truck1)
msc.truck_arrived(truck2)

hour = 0
while spb.content < TOTAL_CARGO:
    hour += 1
    print('---------- Час {} ----------'.format(hour))
    truck1.act()
    truck2.act()
    loader1.act()
    loader2.act()
    msc.act()
    spb.act()
    print(truck1)
    print(truck2)
    print(loader1)
    print(loader2)
    print(msc)
    print(spb)


print('всего затраченно топлива {}'.format(Mashini.total_fuel))