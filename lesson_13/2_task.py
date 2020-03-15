# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента
from contextlib import ContextDecorator


class Context_Decorator(ContextDecorator):
    def __init__(self, *args):
        self.args = args

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.args)


@Context_Decorator(FileNotFoundError, ZeroDivisionError)
def arifmetic(a):
    return a / 0


arifmetic(6)
print('arifmetic - подавлен')

with Context_Decorator(FileNotFoundError, ZeroDivisionError):
    print(1 / 0)
print('Context_Decorator - подавлен')
