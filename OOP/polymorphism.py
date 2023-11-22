# Полиморфизм - принцип ООП, в котором в разных методы называются одинаково, но реализация(функционал) разная (один интерфейс - разный функционал)

1+1
'a'+'a'
[1,2]+[1,2]

# Полиморфизм - множесвто форм
a = 1
a.__add__(4)

class Cat:
    def voice(self):
        print('мяу-мяу')

class Dog:
    def voice(self):
        print('гав-гав')

objects = [Cat(), Dog()]

for i in objects:
    i.voice()

class A:
    def func(self):
        pass

class B(A):
    def func(self):
        pass

# напишите два класса Square, Circle
# в обеих должен быть метод для высчитывания площади(area)
# square = Square(4-сторона)
# circle = Circle(5-радиус)
# square.area() - 16
# circle.area() - 

from math import pi
from abc import ABC, abstractmethod

class ShapeMixin(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Square(ShapeMixin):
    def __init__(self, s) -> None:
        self.side = s
    
    def area(self):
        print(self.side**2)

class Circle(ShapeMixin):
    def __init__(self, r) -> None:
        self.radius = r
    
    def area(self):
        print(pi*(self.radius**2))


# list.pop()
# dict.pop()
# set.pop()

class India:
    def capital(self):
        print("New Delhi is the capital of India")
    
    def language(self):
        print("Hindi is the language of India")
    
    def location(self):
        print("South Asia is the location of India")

class GreatBritan:
    def capital(self):
        print("London is the capital of Greate Britan")
    
    def language(self):
        print("English is the language of Greate Britan")
    
    def location(self):
        print("Europe is the location of Greate Britan")

def func(obj):
    obj.capital()
    obj.language()
    obj.location()

india = India()
britan = GreatBritan()

func(india)
func(britan)

# USA(89-сомов)
# KZ
# exchange()

# напишите два класса машин 
# Toyota
# Lexus
# speed = 180km/h
# speed = 240km/h
# max_speed_20km

# t = S:V
# t = 20//240
# 

class Toyota:
    speed = 180
    km = 20

    def max_speed_20km(self):
        t = self.km/self.speed
        return t * 3604

class Lexus(Toyota):
    speed = 240
    # km = 20

    def max_speed_20km(self):
        t = self.km/self.speed
        minute = t * 60
        return minute

