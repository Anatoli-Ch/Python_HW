# Написать декоратор и менеджер контекста который будет подавлять все ошибки возникающие в теле вашей функции.
from contextlib import ContextDecorator


class Manager(ContextDecorator):
    def __init__(self, f):
        self.f = f

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.f)


@Manager(Exception)
def function(a,  b):
    return (a + b) + 'abc'


with Manager(function):
    print(function(6, 7))
