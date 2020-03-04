# На ввод дается строка. Нужно каждое слово развернуть наоборот. Порядок слов не должен меняться.
enter_string = input('Введите строку: ').split()
lst = []

for i in enter_string:
    lst.append([i[::-1]])

second_string = ' '.join([' '.join(i) for i in lst])

print(second_string)
