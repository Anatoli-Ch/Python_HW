# Реализовать примеры с functools - wraps и singledispatch
from functools import singledispatch, wraps


def dec_function(func):
    """Function in function"""
    @wraps(func)
    def wrapps():
        """decorated function"""
        pass

    return wrapps


@dec_function
def a_function():
    """Simple Function"""
    return 'Hello World!'


@singledispatch
def summer(a, b):
    pass


@summer.register(str)
def _(a, b):
    print(a + b)


@summer.register(int)
def _(a, b):
    print(a - b)


summer('Hello', 'World!')
summer(100, 50)
print(a_function.__name__)
print(a_function.__doc__)
