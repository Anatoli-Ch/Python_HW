# Создайте два класса: Person — хранит общую информацию о людях — имя, профессия, зарплата;
# класс Manager — специализированный производный класс.
# В классе Person создайте свою версию для стандартной встроенной функции str.


class Person:
    def __init__(self, name, profession, salary):
        self.name = name
        self.profession = profession
        self.salary = salary

    def __str__(self):
        return 'name - {}\nprofession - {}\nsalary - {}$'.format(self.name, self.profession, self.salary)


class Manager(Person):
    def __init__(self, name, profession, salary):
        super().__init__(name, profession, salary)


pr = Manager('Vlad', 'Python Developer', 2500)
print(pr)
