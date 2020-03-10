# Создайте класс который будет хранить параметры для подключения к физическому юниту(например switch).
# В своем списке атрибутов он должен иметь минимальный набор (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и сеттеров(@property).
# У вас должна быть возможность получения и назначения этих атрибутов в классе.


class Switch(object):
    def __init__(self):
        self._unit_name = None
        self._mac_address = None
        self._ip_address = None
        self._login = None
        self._password = None

    @property
    def password(self):
        return self._password

    @property
    def login(self):
        return self._login

    @property
    def ip(self):
        return self._ip_address

    @property
    def mac(self):
        return self._mac_address

    @property
    def name(self):
        return self._unit_name

    @password.setter
    def password(self, value):
        self._password = value

    @login.setter
    def login(self, value):
        self._login = value

    @mac.setter
    def mac(self, value):
        self._mac_address = value

    @name.setter
    def name(self, value):
        self._unit_name = value

    @ip.setter
    def ip(self, value):
        self._ip_address = value


switch = Switch()
switch.name, switch.mac, switch.ip, switch.login, switch.password = 'Vlad', 10101, '81.987.476.345', 'open', 12345
print('Unit_name - {}\nMac_address - {}\nip_address - {}\nLogin - {}\nPassword - {}\n'.format(
    switch.name, switch.mac, switch.ip, switch.login, switch.password))
switch.name, switch.mac, switch.ip, switch.login, switch.password = 'Dmitriy', 90345, '90.900.470.300', 'enter', 654789
print('Unit_name - {}\nMac_address - {}\nip_address - {}\nLogin - {}\nPassword - {}'.format(
    switch.name, switch.mac, switch.ip, switch.login, switch.password))
