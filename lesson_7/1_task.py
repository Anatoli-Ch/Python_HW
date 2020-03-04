# Реализовать все декораторы - таймер, запоминатель, счетчик вызовов и единичный вызов
import time


def once_dec(func):
    def inner(*args, **kwargs):
        if not inner.called:
            print('really doing init')
            func(*args, **kwargs)
            inner.called = True
        else:
            print('not first init')

    inner.called = False
    return inner


def tracer(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {} to {}'.format(calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


def memory(f):
    cache = {}

    def decorate(*args):
        print(args)
        if args not in cache:
            print('args not in cache')
            cache[args] = f(*args)
        return cache[args]

    return decorate


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print('Время выполнения функции: {}'.format(time.time() - t))
        return res

    return tmp


@once_dec
@tracer
@memory
@timer
def working(x, y):
    lst = []
    while x != y:
        x += 1
        lst.append(x)
    return len(lst)


print(working(0, 100_000))
