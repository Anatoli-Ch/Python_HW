# Дан список словарей autos. Нужно их отсортировать.
# по стоимости, от больших к меньшим
# использовать для сортировки лямбду и обычную функцию
from operator import itemgetter
autos = [

    {"brand": "Ford", "model": "Mustang", "year": 1964, 'price': 4000},

    {"brand": "Ford", "model": "Mondeo", "year": 1999, 'price': 3000},

    {"brand": "Ford", "model": "Fiesta", "year": 2003, 'price': 4200},

    {"brand": "Nissan", "model": "Primera", "year": 1997, 'price': 3100},

    {"brand": "BMW", "model": "X3", "year": 2001, 'price': 5000},

    {"brand": "Nissan", "model": None, "year": 1964, 'price': None},

    {"brand": "VW", "model": "Passat", "year": 1996, 'price': 1200},

    {"brand": "BMW", "model": "X5", "year": 2010, 'price': 7500},

    {"brand": "Renault", "model": "Megane", "year": 1999, 'price': 2300},

 ]


def sorted_func(dic):
    value = dic['price']
    if value is None:
        return 0
    else:
        return value


first_sort = sorted(autos, key=sorted_func, reverse=True)
for j in first_sort:
    print("{}".format(j))

print()
new_sort = sorted(autos, key=lambda k: k['price'] if k['price'] is not None else 0, reverse=True)
for i in new_sort:
    print("{}".format(i))
