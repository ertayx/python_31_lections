# магические методы - это в первую очередь те методы которые имеют __ __, срабатывают они при выполнении операции >< *-.== + / ** %
# dunder methods - double underscore methods

# new - конструктор класса, отвечает за создание обьекта
# init - инициализатор класса, задает созданному обьекту аттрибуты
# del - деструктор класса, отвечает за удаление обьекта

# class User:
#     def __new__(cls, *args, **kwargs):
#         print('new worked: ')
#         return super().__new__(cls)
    
#     def __init__(self, name, email) -> None:
#         print('init worked: ')
#         self.name = name
#         self.email = email
    
#     def __del__(self):
#         print('del worked: ')

# user = User('Nikita', 'nikita@gmail.com')


# from typing_extensions import SupportsIndex


class MyInt(int):
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other: int) -> int:
        return f'Это сложение и результат равен:{self.value + other}'
    
    def __sub__(self, other: int) -> int:
        return f'Это вычитание и результат равен:{self.value - other}'

    def __mul__(self, other: int) -> int:
        return f'Это умножение и результат равен:{self.value * other}'
    
    def __truediv__(self, other: int) -> float:
        return f'Это деление(/) и результат равен:{self.value / other}'
    
    def __floordiv__(self, __value: int) -> int:
        return super().__floordiv__(__value)
        
    def __lt__(self, other: int) -> bool: # lower than
        return f'Это знак < {self.value<other}'
    def __gt__(self, other: int) -> bool: # greater than
        return f'Это знак > {self.value>other}'
    def __eq__(self, other: object) -> bool:
        return f'Это знак == {self.value == other}'
    def __ne__(self, other: object) -> bool:
        return f'Это знак != {self.value == other}'
    def __le__(self, __value: int) -> bool:
        return '<='
    def __ge__(self, __value: int) -> bool:
        return '>='
    # ** - __pow__
    # % - __mod__
    # > - __gt__

obj_int = MyInt(5)
print(obj_int<9)
print(obj_int>4)
print(obj_int==5)
# print(dir(obj_int))

# в чем отличие методов с буквой r в начале и без

# написать класс MyInt который принимает значение 
# все сравнивания в этом классе работают наоборот
# 5==5 - false
# 6>5 - false
# 6<5 - true

class MyInt(int):
    def __init__(self, value) -> None:
        self.value = value

    def __lt__(self, __value: int) -> bool:
        return self.value > __value
    
    def __gt__(self, __value: int) -> bool:
        return not self.value>__value
    
    def __eq__(self, __value: int) -> bool:
        return not self.value==__value
    
    def __ne__(self, __value: int) -> bool:
        return not self.value!=__value

# __getitem__
# a = 'asdf'
# a[0]
# dict_ = {'a':5}
# dict_.__getitem__('a')
class MyStr(str):
    def __init__(self, value) -> None:
        self.value = value

    def __getitem__(self, __key) -> str:
        __key+=1
        return super().__getitem__(__key)
    
    def __setitem__(self, __key, new):
        old = self.value[__key]
        self.value = self.value.replace(old, new)

    def __str__(self) -> str:
        return self.value

mystr = MyStr('Nikita')
# print(mystr[0])
mystr[3] = 'tt'
print(mystr)

mystr.value
# __getatribute__
# getattr

dect_ = {'a':5}
dect_['b']
dect_.get('b')