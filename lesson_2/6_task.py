# Дана строка "English = 78 Science = 83 Math = 68 History = 65".
# Вычислить сумму всех чисел в строке.
import re

starting_string = 'English = 78 Science = 83 Math = 68 History = 65'
summ = sum(map(int, re.findall('(\d+)', starting_string)))
print('Сумма всех чисел строки -', summ)
