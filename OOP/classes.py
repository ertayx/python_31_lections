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
