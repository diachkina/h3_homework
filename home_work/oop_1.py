"""У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13) ''
"""


class IpHandler:
    """Обрабатывает список IP-адресов, каждый IP-адрес должен быть строкой"""
    def __init__(self, ip_list):
        self.ip_list = ip_list

    @property
    def ip_list(self):
        return self._ip_list

    @ip_list.setter
    def ip_list(self, new_list):
        for ip in new_list:
            if not isinstance(ip, str):
                raise TypeError('IP-address must be in <class str>')
        self._ip_list = new_list

    def reverse_IP(self):
        """Вернуть обратный IP-адрес"""
        reversed_list = list(map(lambda ip: '.'.join(reversed(ip.split('.'))), self.ip_list))
        return reversed_list

    def get_oct_1_3(self):
        """Возвращает список IP-адресов без первых октетов (127.0.0.1 -> .0.0.1)"""
        ip_list_1_3oct = []
        for ip in self.ip_list:
            ip_list_1_3oct.append(ip.split('.'))
        for a in ip_list_1_3oct:
            a.pop(0)
        ip_list_1_3oct = list(map(lambda p: '.'.join(p), ip_list_1_3oct))
        return ip_list_1_3oct

    def get_oct_3(self):
        """Возвращает список последних октетов каждого IP-адреса (127.0.0.1 -> .1)"""
        ip_list_3oct = []
        for ip in self.ip_list:
            ip_list_3oct.append(ip.split('.')[-1])
        return ip_list_3oct


add = IpHandler(['10.11.12.13', '20.21.22.23', '30.31.32.33', '40.41.42.43'])
print(add.reverse_IP())
print(add.get_oct_1_3())
print(add.get_oct_3())


"""Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе."""
print()
print()
print()

class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, name):
        if not name.isdigit():
            self._unit_name = name
        else:
            print('Please use only letters')

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, address):
        if not len(address) != 12:
            self._unit_name = address
        else:
            print('Please enter a right address')

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip):
        if not ip.isalpha():
            self._ip_address = ip
        else:
            print('Wrong IP-address')

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, logname):
        if not len(logname) < 8:
            self._login = logname
        else:
            print('Your login is too short')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, key):
        if not len(key) < 6:
            self._password = key
        else:
            print('Your password is too short')


q = ConnHandler()
q.unit_name = '456789'
print(q.unit_name)
print(q.mac_address)
print(q.ip_address)
print(q.login)
print(q.password)

# unit_name='', mac_address='', ip_address='', login='', password='')