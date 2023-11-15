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
# print(a._protected) # мы не должны обращаться к защ.аттрибуту или методу через объект (на уровне соглашения)
# print(a.__private) # к приватному аттрибуту я не могу обратится через объект и дочерних классов
# _<название класса>__<название метода(аттр.)> (так нельзя на уровне соглашения)

class B(A):
    def func(self):
        self.public
        # self.__private_func()

# b = B()
# b.func()
# print(b._A__private) # так нельзя на уровне соглашения

class Person:
    name = 'Nikita'
    __last_name = 'Grebnev'

    def get_last_name(self):
        # return f'My name is {self.name}, ny last name is {self.__last_name}'
        return self.__last_name
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
    
# human = Person()
# # human._Person__last_name = 'Zhoroev'
# print(human.get_last_name())
# human.set_last_name('Zhoroev')
# print(human.get_last_name())

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
    # __setattr__ - 
    def level(self, n):
        self.__level = n

# game = Game()
# propety | level.getter
# print(game.get_level())
# game.set_level(90)
# print(game.get_level())
# print(game._Game__level)
# game._Game__level = 89
# print(game._Game__level)
# print(game.level)
# game.level = 90
# print(game.level)
# game.level = 78
# print(game.level)


# написать класс Human который принимает чз экземпляр следующие аттрибуты: name, age, last_name
# превратить name в защищенный аттрибут
# превратить age в приватный аттрибут
# добавить возможность получать и изменять приватный аттрибут(getter & setter)

# class Human:
#     def __init__(self, name, age, last_name) -> None:
#         self._name = name
#         self.__age = age
#         self.last_name = last_name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, n):
#         self.__age = n

# human = Human('name', 78, 'last_name')
# print(human.age)
# human.age += 1
# print(human.age)

# _create_user
# create_user
# create_superuser

class A:
    _a = 7
    # getter - переопределяет маг.метод __getattribute__
    # setter - переопределяет маг.метод __setattr__
    # deleter - переопределяет маг.метод __delattr__

# a = A()
# print(a._a)
# print(a.__getattribute__('_a'))
# a._a = 5
# a.__setattr__('_a', 5)
# print(a.__getattribute__('_a'))
# a.__setattr__('a', 6)
# print(a._a)

class Human:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.deleter # срабатывает когда пишем оператор "del"
    def name(self):
        del self.__name

human = Human('Nikita')
print(human.name)
del human.name

# class Temp
# target_temp
# default_temp
# default_temp = 7
# target_temp = 20
# add_temp - добавляет в default_temp + 1
# minus_temp - отнимает с default_temp - 1
# вы дошли до планновой задачи
# get_temp - получает default_temp

class Temp:
    def __init__(self, target_temp) -> None:
        self.__target_temp = target_temp
        self.__default_temp = 10
        self.doiti_do_target_temp()
    
    def add_temp(self):
        self.__default_temp += 1
        if self.__default_temp == self.__target_temp:
            return 'вы дошли до планновой задачи'

    def minus_temp(self):
        if self.__default_temp == self.__target_temp:
            return 'вы дошли до планновой задачи'
        self.__default_temp -= 1

    def get_temp(self):
        return f'{self.__default_temp} - {self.count} вызвали метод {self.method}'
    
    def doiti_do_target_temp(self):
        self.count = 0
        if self.__target_temp>self.__default_temp:
            for i in range(self.__target_temp-self.__default_temp):
                self.add_temp()
                self.method = self.add_temp.__name__
                self.count+=1
        elif self.__target_temp<self.__default_temp:
            for i in range(abs(self.__target_temp-self.__default_temp)):
                self.minus_temp()
                self.method = self.minus_temp.__name__
                self.count+=1
        else:
            self.count = 0
            self.method = 'не воспользовались метод'
            
temp = Temp(7)
# temp.default_temp = 10
print(temp.get_temp()) # self.__default_temp - 10 вызвали метод add_temp
# вы дошли до планновой задачи
# print(temp.add_temp())

# 7-10 = -3