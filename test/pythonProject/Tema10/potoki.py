# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.

import time
from threading import Thread

number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
def potok(simbol):
    for simbol in simbol:
        time.sleep(1)
        print(simbol)


thread = Thread(target=potok, args=(number,))
thread_2 = Thread(target=potok, args=(letter,))
thread.start()
thread_2.start()

thread.join()
thread_2.join()