#  Дан список студентов.
#  Каждая запись содержит имя студента, и его оценки по физике, математике и химии.
#  Нужно сохранить данные в словарь и по вводимому имени выводить среднюю оценку по всем трем предметам.
#  Пример - список [[‘Krishna’, 67, 68, 69], [‘Arjun’, 70, 98, 63], [‘Malika’, 52, 56, 60]].
#  Если на вход придет имя Malika - ответ будет 56.00.

enter = input('Введите Имя Студента: ')
students = [['Krishna', 67, 68, 69], ['Arjun', 70, 98, 63], ['Malika', 52, 56, 60]]
students2 = []

for i in students:
    res = sum(i[1:]) / 3
    students2.append(i[0])
    students2.append(res)

i = iter(students2)
students_dict = dict(zip(i, i))

print(enter, '=', students_dict.get(enter))
