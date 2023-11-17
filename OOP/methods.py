"существует 3 вида методов"
# instance method
# class method
# static method

class A:
    def instance_method(self):
        print('метод объекта')
        print(f'первый аргумент {self}')

obj = A()
obj.instance_method() # если вызываем у обьекта, то self передается автоматически
A.instance_method(obj) # если вызываем у класса, то self нужно передать объект этого класса

# instance method - обычные методы, которые первым аргументом принимают self (ссылка на объект), нужны они для работы с аттрибутами объекта

class B:
    @classmethod
    def class_method(cls):
        print('метод класса')
        print(f'первый аргумент {cls}')

obj = B()
obj.class_method()
B.class_method()
# не важно откуда вызываем classmethod первым аргументом всегда прилетает ссылка на класс

class A:
    counter = 0 

    def __init__(self) -> None:
        self._increment()

    @classmethod
    def _increment(cls):
        cls.counter+=1

class B(A):
    counter = 0


class Pizza:
    def __init__(self, radius, *ingredients) -> None:
        self.radius = radius
        self.ingredients = ingredients

    @classmethod
    def four_cheeze(cls, r):
        pizza = cls(r, 'Моцарелла', 'Чеддер', 'Дорблю', 'Голладский')
        return pizza
    
    def get_info(self):
        return f'пицца {self.radius*2} ингредиенты {self.ingredients}'

pizza1 = Pizza(20, 'сыр', 'колбоса', 'помидор')
# pizza2 = Pizza(15, 'Моцарелла', 'Чеддер', 'Дорблю', 'Голладский')
# pizza3 = Pizza(30, 'Моцарелла', 'Чеддер', 'Дорблю', 'Голладский')
pizza2 = Pizza.four_cheeze(15)
pizza3 = Pizza.four_cheeze(30)

list_ = [pizza1, pizza2, pizza3]
for i in list_:
    print(i.get_info())

# class methods - методы класса, которые принимают первым аргументом cls (ссыдку на класс), нужны они для изменения аттрибутов и создания обьектов, что бы сохдать класс метод мы должны задекорировать его classmethod

class C:
    @staticmethod
    def static_method(a, b):
        print('статичный метод')
        print('не принимает ни self ни cls (принимает то что нужно)')

from math import pi

class Cylender:
    def __init__(self, diametr, height) -> None:
        self.diametr = diametr
        self.height = height
        self.area = self.get_area(diametr, height)

    @staticmethod
    def get_area(d, h):
        return pi * ((d/2)**2) * h

cylender = Cylender(4, 10)
print(cylender.area)

# написать класс Iphone15 который принимает в себя имя и цену телефона
# написать класс метод change_cost, который меняет цену телефона - принимает новую цену
# написать статичный метод som_to_dollar который принмает цену в сомах и выдает в долларах

class Iphone15:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost

    @classmethod
    def change_cost(cls, new_cost):
        cls.cost = new_cost
        return cls.cost
    
    @staticmethod
    def som_to_dollar(cost):
        print(cost/89.140)
        return cost/89.140

iphon = Iphone15('pro max', 118000)
print(iphon.change_cost(110000))
iphon.som_to_dollar(110000) # 1234.013910702266

# static method - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с объктом, они находятся внутри класса лишь для использования только внутри класса, что бы создать статичный метод его нужно задекорировать staticmethod
