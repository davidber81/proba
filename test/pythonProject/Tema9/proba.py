import time

def time_track(func, *args, **kwargs):
    started_at = time.time()

    result = func(*args, **kwargs)

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return result

def digits(*args):
    total = 1
    for number in args:
        total *= number ** 300
    return len(str(total))

result = time_track(digits,3141, 5926, 2718, 2818)
print(result)