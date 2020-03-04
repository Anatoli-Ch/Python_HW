# Напишите генератор случайных паролей.
# После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
# Завершить программу нужно если будет введен 0.
# Также нужно проверять является ли введенная строка числом.
# Допустимые символы - цифры, большие и маленькие латинские буквы.
# (нужно использовать метод input)
import random

try:
    enter = int(input('Введите длину пароля: '))
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

    while enter != 0:
        for i in range(enter):
            print(random.choice(base), end='')
        enter = int(input('\nВведите длину пароля: '))

except ValueError:
    print('Длина пароля задается только числом')
