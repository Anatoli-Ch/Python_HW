# Реализовать дескриптор валидации для атрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить.


class EmailDescriptor:
    def __get__(self, instance, owner):
        print(instance, owner)

    def __set__(self, instance, value):
        base = []
        for i in value:
            if i == '@' or i == '.':
                base.append(i)
        if len(base) > 2 or len(base) == 0 or len(base) < 2:
            print(value, '-', False)
        else:
            print(value, '-', True)


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
my_class.email = "de@mail@gmail.com."
my_class.email = "novalidemail"
print(my_class)
