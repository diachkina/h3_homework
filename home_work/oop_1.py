'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13) ''
'''


class IpHandler:
    "" "Обрабатывает список IP-адресов, каждый IP-адрес должен быть строкой" ""
    def __init__(self, ip_list):
        self.ip_list = ip_list

    @property
    def ip_list(self):
        return self.ip_list

    @ip_list.setter
    def ip_list(self, new_list):
        self.new_list = new_list


    def reverse_IP(self, ip_list, new_list):
        "" "Вернуть обратный IP-адрес"
        self.reverse_IP = new_list
        new_list = list(map(lambda ip: '.'.join(reversed(ip.split('.'))), ip_list))
        return new_list


    def get_oct_1_3(self, ip_list):
        "Возвращает список IP-адресов без первых октетов (127.0.0.1 -> .0.0.1)"
        ip_list_1_3oct = []
        for ip in ip_list:
            ip_list_1_3oct.append(ip.split('.'))
        for a in ip_list_1_3oct:
            a.pop(0)
        ip_list_1_3oct = list(map(lambda p: '.'.join(p), ip_list_1_3oct))
        return ip_list_1_3oct


    def get_oct_3(self, ip_list):
        "Возвращает список последних октетов каждого IP-адреса (127.0.0.1 -> .1)"
        ip_list_3oct = []
        for ip in ip_list:
            ip_list_3oct.append(ip.split('.')[-1])
        return ip_list_3oct


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password