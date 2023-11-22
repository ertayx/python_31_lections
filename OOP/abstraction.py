# Абстракция - принцип ООП, в котором создается класс пустышка, где задаются названия аттрибутов и методов, для того, чтобы в дочерних классах не забыть их переопределить

from abc import ABC, abstractmethod, abstractproperty

class A(ABC):
    @abstractmethod
    def func(self):
        pass

    @abstractproperty
    def a(self):
        pass

class B(A):
    a = 8
    # pass
    def func(self):
        print('B')
b = B()


class AbstractAnimal(ABC):
    @abstractmethod
    def voice(self):
        pass
    
    @abstractproperty
    def legs(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(AbstractAnimal):
    legs = 4
    def voice(self):
        print('гав-гав')
    def move(self):
        print('walk')

# dog = Dog()

class Bird(AbstractAnimal):
    legs = 2
    def voice(self):
        print('фью-фью')
    def move(self):
        print('fly')

bird = Bird()

# написать абстрактный класс Shape, в котором есть абстрактные методы calculate_area, calculate_perimeter, angle
# написать класс Sqaure который наследуется от Shape
# и высчитывает площадь и периметр квадрата
# написать класс Triangle который наследуется от Shape
# и высчитывает площадь и периметр трехугольника

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractproperty
    def angle(self):
        pass
import math

class Triangle(Shape):
    angle = 3

    def __init__(self, side1, side2, side3) -> None:
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1+self.side2+self.side3) / 2
        return math.sqrt(s * (s-self.side1) * (s-self.side2) * (s-self.side3))
    
    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3

class Square(Shape):
    angle = 4
    def __init__(self, side) -> None:
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return self.side * self.angle

triangle = Triangle(1, 2, 3)

triangle.calculate_area()
triangle.calculate_perimeter()

# s = (side1+side2+side3) / 2
# sqrt(s * (s-side1) * (s-side2) * (s-side3))

# side1+side2+side3

class PaymentSystem(ABC):
    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractproperty
    def balance(self):
        pass

class CreditCard(PaymentSystem): # через экземпляр класса принять номер карты и срок действия
    balance = 1000
    
    def __init__(self, card_number, expiry_date) -> None:
        self.card_number = card_number
        self.expiry_date = expiry_date

    def make_payment(self, amount):
        if amount>self.balance:
            raise Exception('не хватает средств')
        self.balance-=amount
    def get_balance(self):
        return self.balance

class MBank(PaymentSystem): # через экземпляр класса принять номер телефона и пароль
    balance = 2000

    def __init__(self, phone_number, password) -> None:
        self.phone_number = phone_number
        self.password = password

    def make_payment(self, amount):
        if amount>self.balance:
            raise Exception('не хватает средств')
        self.balance-=amount

    def get_balance(self):
        return self.balance


class A(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

class B(A):
    def __init__(self) -> None:
        pass

b = B()