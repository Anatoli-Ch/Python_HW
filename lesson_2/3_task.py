# На ввод подается строка. Нужно узнать является ли строка палиндромом.
# (Палиндром - строка которая читается одинаково с начала и с конца.)
enter_string = input('Введите строку: ').lower()
lst = []

for i in enter_string:
    lst.append(i)
lst.reverse()

second_string = ''.join(lst)

if second_string == enter_string:
    print('Это Палиндром!')
else:
    print('Это не Палиндром!')
