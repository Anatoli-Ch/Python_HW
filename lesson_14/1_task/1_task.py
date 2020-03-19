# Реализовать свой класс исключения. Добавить метод записи в файл.
# Вызвать своё исключение и записать ошибку в файл.


class MyException(Exception):
    def __init__(self, elements):
        self.elements = elements

    def __enter__(self):
        pass

    @staticmethod
    def write_to_file(elem):
        with open('result.txt', 'w') as f:
            f.write(str(elem))


def func(a, b):
    try:
        if b == 0:
            raise MyException('ZeroDivisionError.')
    except MyException as mr:
        mr.write_to_file(b)
        return
    else:
        print(b)
    return a / b


b = 0
print(func(5, b))
