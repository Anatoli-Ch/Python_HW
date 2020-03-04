# Дается строка - нужно проверить является ли она валидным паролем:
# длина больше 4 символов
# содержит только маленькие латинские буквы и цифры
# число букв должно быть нечетным, а цифр четным.

enter = input('Введите пароль: ')


def check(password):
    base_num = []
    base_letr = []
    if len(password) < 4:
        return 'пароль слишком короткий'
    for i in password:
        if i in '1234567890':
            base_num.append(i)
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 'Буквы в пароле должны быть в нижнем регистре'
        elif i in 'abcdefghijklmnopqrstuvwxyz':
            base_letr.append(i)
        else:
            return 'Ваш павроль содержит запрещенные символы'

    if len(base_letr) % 2 == 0:
        return 'Количество букв должно быть нечетным'
    elif len(base_num) % 2 != 0:
        return 'Количество цифр должно быть четным'

    return 'Ваш пароль является Валидным - {}'.format(password)


print(check(enter))
