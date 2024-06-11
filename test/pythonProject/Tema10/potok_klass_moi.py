import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill

    def run(self):
        voin = 100
        print(f'{self.name}, начинает защищать королевство.')
        day = 0
        while voin != 0:
            voin -= self.skill
            day += 1
            print(f'{self.name}, сражается, {day} день(дня)..., осталось {voin} воинов.')
            time.sleep(day)
            if voin == 0:
                print(f'{self.name}, защитил королевство за {day} дней.')

knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')