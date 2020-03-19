# Использовать contextmanager и реализовать функцию, которая будет работать как менеджер контекста.
# И сможет замерять время выполнения блока
from contextlib import contextmanager
import time


@contextmanager
def context_manager(num):
    start = time.time()
    print('Enter')
    yield num + 1
    end = time.time()
    interval = end - start
    print(interval)
    print('Exit')


with context_manager(2) as cm:
    print(cm)
