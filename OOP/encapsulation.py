# Инкапсуляция:
# Ограничение доступа к методам и аттрибутам (соурытие данных)
# Сбор всех методов и аттрибутов в одну капсулу(класс)

# 3 модификатора доступа
# public - публичный
# protected - защищенный
# private - приватный

class A:
    public = 'публичный'
    _protected = 'защищенный'
    __private = 'приватный'

    def public_func(self):
        self.__private_func()
    def _protected_func(self):pass
    def __private_func(self):pass

a = A()
print(a._protected) # мы не должны обращаться к защ.аттрибуту или методу через объект (на уровне соглашения)
# print(a.__private) # к приватному аттрибуту я не могу обратится через объект и дочерних классов
# _<название класса>__<название метода(аттр.)> (так нельзя на уровне соглашения)

class B(A):
    def func(self):
        self.public
        # self.__private_func()

b = B()
b.func()
print(b._A__private) # так нельзя на уровне соглашения

class Person:
    name = 'Nikita'
    __last_name = 'Grebnev'

    def get_last_name(self):
        # return f'My name is {self.name}, ny last name is {self.__last_name}'
        return self.__last_name
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
    
human = Person()
# human._Person__last_name = 'Zhoroev'
print(human.get_last_name())
human.set_last_name('Zhoroev')
print(human.get_last_name())

# написать класс Game в котором есть приватный аттрибут level
# добавить в класс Game возможность получать и изменять аттрибут level

class Game:
    __level = 0

    # def get_level(self):
    #     return self.__level
    
    # def set_level(self, n_level):
    #     self.__level = n_level
    @property # превращает метод в аттрибут
    def level(self):
        return self.__level
    
    @level.setter # позволяет изменить аттрибут
    def level(self, n):
        self.__level = n

game = Game()
# propety | level.getter
print(game.get_level())
game.set_level(90)
print(game.get_level())
print(game._Game__level)
game._Game__level = 89
print(game._Game__level)
print(game.level)
game.level = 90
print(game.level)
game.level = 78
print(game.level)


# написать класс Human который принимает чз экземпляр следующие аттрибуты: name, age, last_name
# превратить name в защищенный аттрибут
# превратить age в приватный аттрибут
# добавить возможность получать и изменять приватный аттрибут(getter & setter)

class Human:
    def __init__(self, name, age, last_name) -> None:
        self._name = name
        self.__age = age
        self.last_name = last_name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, n):
        self.__age = n

human = Human('name', 78, 'last_name')
print(human.age)
human.age += 1
print(human.age)

# _create_user
# create_user
# create_superuser