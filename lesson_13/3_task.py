# Создать менеджер контекста который будет подсчитывать время выполнения блока инструкций
import time
import urllib.request


class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print('{} за: {} секунд'.format(self.name, self.interval))
        return False


with Timer('Выполнено'):
    conn = urllib.request.urlopen('https://www.python.org/')
