# Реализовать дескриптор валидации для атрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить.
import re


class EmailDescriptor:
    def __get__(self, instance, owner):
        print(instance, owner)
        return owner

    def __set__(self, instance, value):
        base = "^[_A-Za-z0-9-\\+]+(\\.[A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
        if re.match(base, value):
            print(value, '-', True)
            return value
        else:
            print(value, '-', False)
            # raise Exception('email is invalid')


class MyClass:
    base = EmailDescriptor()
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
my_class.email = "de@mail@gmail.com."
my_class.email = "novalidemail"
my_class.email = "vs/got@gmail.com"
print(my_class)
