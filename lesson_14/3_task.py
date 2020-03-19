# Реализовать класс который можно использовать и как декоратор и как менеджер контекста
# Пусть он тоже замеряет время выполнения.
# Проверить что работает быстрее - вызвать и обработать исключение или использовать условный оператор
import time


def func(f1, f2):
    if f1 < f2:
        return 'try - except is faster!'
    else:
        return 'operator "if" is faster!'


class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.start = time.time()
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.finish = time.time()
        self.interval = self.finish - self.start
        self.open_file.close()
        print('result - ', self.interval)


start_time1 = time.process_time()

try:
    with File('file.txt', 'a') as f:
        count = 0
        for _ in range(10000):
            f.write(' foo bar, ')
            count += 1
            if count == 9999:
                raise TimeoutError('To many iterations!...')
except TimeoutError:
    pass

res1 = (time.process_time() - start_time1)
start_time2 = time.process_time()

with File('file.txt', 'w') as f:
    count = 0
    for _ in range(1000):
        f.write(' foo bar, ')
        count += 1
        if count == 9999:
            raise TimeoutError('To many iterations!...')
        if TimeoutError:
            pass

res2 = (time.process_time() - start_time2)

print(func(res1, res2))
