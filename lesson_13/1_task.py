# Написать декоратор и менеджер контекста который будет подавлять все ошибки возникающие в теле вашей функции.
from functools import partial


class Opened:
    def __init__(self, *args, **kwargs):
        self.worker = partial(summer, *args, **kwargs)

    def __enter__(self):
        print('enter')
        self.handle = self.worker()
        return self.handle

    def __exit__(self, exc_type, exc_val, exc_tb):  # exc_type = тип исключения exec_val = значение исключени
        self.handle.close()  # exec_tb = то что привело к этому исключению
        del self.handle
        print('exit')


def summer(f1, f2):
    return f1 + f2


with Opened(summer(10, 15)) as handle:
    pass
