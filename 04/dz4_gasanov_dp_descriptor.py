#2. Дескрипторы с проверками типов и значений данных (+тесты)


class Integer:
    def __init__(self):
        self.num = 0

    def __get__(self, instance, owner):
        return self.num

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.num = value
        else:
            raise TypeError

    def __delete__(self, instance):
        del self.num


class String:
    def __init__(self):
        self.str_ = 0

    def __get__(self, instance, owner):
        return self.str_

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.str_ = value
        else:
            raise TypeError

    def __delete__(self, instance):
        del self.str_


class PositiveInteger:
    def __init__(self):
        self.pos_int = 0

    def __get__(self, instance, owner):
        return self.pos_int

    def __set__(self, instance, value):
        if isinstance(value, str) or value < 0:
            raise TypeError
        self.pos_int = value

    def __delete__(self, instance):
        del self.pos_int


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num=10, name='Bar', price=100):
        self.num = num
        self.name = name
        self.price = price
