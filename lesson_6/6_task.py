# Дан список из чисел. Нужно реализовать подсчет суммы чисел на отрезке списка.
# На вход даются запросы в виде пары чисел
# - индекс начала и конца интервала для суммирования
# - нужно выводить сумму элементов списка для каждого запроса.
# * Как это реализовать если список длиной больше 1 млн и запросов больше 1 млн ?

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [i for i in range(1, 1_000_000)]

while True:
    x, y = int(input("введите индекс начала: ")), int(input("введите индекс конца: "))
    # result = sum(lst[x:y])
    result2 = sum(lst2[x:y])
    # print(result)
    print(result2)
