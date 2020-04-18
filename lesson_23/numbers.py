# Выберите класс из пердыдущих дз и покройте его тестами. Не сильно сложное, но чтоб был какой-то функционал.
# Можно использовать любой фреймворк для тестов или даже несколько.
# Предпочтительно pytest.


class Numbers(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
