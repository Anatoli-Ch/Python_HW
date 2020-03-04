# Реализовать свой lru_cache
from functools import lru_cache


@lru_cache(maxsize=None)
def some_func(x, y):
    lst = []
    while x != y:
        x += 1
        lst.append(x)
    lst = sum(lst)
    return sum([int(d) for d in str(lst)])


print(some_func(0, 563783))
print(some_func.cache_info())
