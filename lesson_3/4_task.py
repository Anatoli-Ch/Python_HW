# Сортировать список от меньшего к большему с помощью heapq
import heapq


def sorting_func(iterable):
    lst = []
    for value in iterable:
        heapq.heappush(lst, value)
    return [heapq.heappop(lst) for _ in range(len(lst))]


my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print(sorting_func(my_list))
