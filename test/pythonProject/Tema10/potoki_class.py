import time
from threading import Thread
class Knight(Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
    def run(self):
        voin = 100
        days = voin // self.skill
        print(f'{self.name}, начинает защищать королевство.')
        print(f'{self.name}, защитит королевство за {days} дней.')
        time.sleep(days)
knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')