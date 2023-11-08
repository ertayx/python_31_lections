"============OOP============"
# class - шаблон (схема)
# обьект, экземпляр, instance - обьект, созданный по шаблону класса (перенимает все аттрибуты и методы класса)

# аттрибут класса - переменные внутри класса (которые будут присвоены каждму обьекту)
# аттрибут экземпляра класса - переменные внутри класса которые мы принимаем при созданни экземпяра (обьекта)
# метод - функция внутри класса
# self - ссылка на сам класс
# __init__ - маг. метод конструктор, который создает новые аттрибуты внутри класса

# SOLID

class Car:
    shifter = 'коробка передачи' # аттрибут класса
    engine = 'двигатель'
    speedometr = 'speedometr'

    def __init__(self, color, qauntity_of_door) -> None: # __init__
        self.color = color # аттрибут экземпляра класса
        self.qauntity_of_door = qauntity_of_door

    def move(self):
        print('Whruuuum')
    
    def start(self):
        print('turn on')
    
    def end(self):
        print('turn off')

car1 = Car('черный', 4)

# print(car1.engine)
# car2 = Car('белый', 2)
# print(car2.engine)
# car3 = Car('красный', 3)
# print(car3.engine)

class Human:
    legs = 2
    arms = 2
    eyes = 2

    def __init__(self, nation, language, race, gender, hair_color) -> None:
        # Human.nation = nation
        self.nation = nation
        self.language = language
        self.race = race
        self.gender = gender
        self.hair_color = hair_color

    def think(self, about='не о чем'):
        self.a = 5
        print(f'думаю о {about}')
    
    def voice(self):
        print('blah blah blah')
    
    def sleep(self):
        print('z z z z')

    def walk(self):
        print('хожу')
    
    def breath(self):
        print('дишу')
    
    def get_info(self):
        return f'Моя страна {self.nation}, мой язык {self.language}, мой пол - {self.gender}, моя расса {self.race}, мой цвет волос {self.hair_color}'

human1 = Human('Россия', 'русский', 'европиоидная', 'оно', 'розовый')
# print(type(type(human1)))
# print(type(type))
print(type(human1.__class__)) # мета классы

# human2 = Human('Кыргызстан', 'кыргызский', 'монголоидная', 'мужик', 'черный')
# human3 = Human('Нигерия', 'нигерийский', 'негроидная', 'женщина', 'кожанный')

# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация


# написать калькулятор на классах 
class Calc:

    def plus(self, num1, num2):
        return num1 + num2
    
    def minus(self, num1, num2):
        return num1 - num2
    
    def mul(self, num1, num2):
        return num1 * num2
    
    def div(self, num1, num2):
        return num1 / num2
    
obj = Calc()
print(obj.div(2,3))
print(obj.minus(3,4))

class Animal:
    eyes = True
    heart = True
    brain = True
    instaincts = True

    def __init__(self, name, type_, isbeast:bool, sex) -> None:
        self.name = name
        self.type = type_
        self.isbeast = isbeast
        self.sex = sex

    def breath(self):
        print('breath')
    
    def get_info(self):
        print(f'I am {self.name}, my type is {self.type}')

# наисать класс ToDo
# класс хранит в себе информацию о делах экземпляра
# написать метод для получения всех дел экземпляра
# написать метод для добавления новых дел и приоритетов


class ToDo:

    data_base = []

    def add_todo(self, todo, prioritet):
        self.data_base.append({prioritet:todo})        

    def get_todo(self, prioritet:int=0):
        if prioritet:
            result = []
            for i in self.data_base:
                if not i.get(prioritet):
                    continue
                result.append(i.get(prioritet, ))
            return result
        else:
            result = [i for i in self.data_base]
            return result
    
    def search(self, title):
        for i in self.data_base:
            for k, v in i.items():
                if not v == title:
                    continue
                return {k:v}
        return 'не найдено'

human = ToDo()
human.add_todo('упасть', 2)
human.add_todo('учится', 3)
human.add_todo('родится', 1)
human.add_todo('пп', 2)
print(human.search('упаст')) # {2: 'упасть'}
# print(human.get_todo(2))

# написать класс Math
# в котором есть метод get_sqrt
# который принимает число выводит квадратный корень числа

class Math:
    result = 0

    def __init__(self, number) -> None:
        f = self.get_factorial(number)
        self.result = self.get_sqrt(f)

    def get_factorial(self, number):
        if number == 1:
            return 1
        return number * self.get_factorial(number-1)

    def get_sqrt(self, number):
        return number**0.5
    

obj = Math(4)
print(obj.result)

# написать итерируемый integer