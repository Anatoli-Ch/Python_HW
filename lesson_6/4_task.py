# Поиск минимума с переменным числом аргументов в списке.
# def min(*args): ....

enter = [10, 20, 35, 5, 6, 2, 7, 15]


def min(*args):
    base_list = args
    sorted_list = []
    for i in base_list:
        for j in i:
            sorted_list.append(j)
    result = sorted(sorted_list)
    return result[0]


print(min(enter))
