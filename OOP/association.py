# Ассоциация - Принцип ООП, в котором два класса связанны друг с другом
# агрегация - слабая связь
# композиция - сильная связь

class Battery:
    _power = 100

    def charge(self):
        self._power = 100

class Iphone:
    def __init__(self, color='черный') -> None:
        self.color = color
        self.battery = Battery()
        # композиция
    def spend_power(self):
        self.battery._power -= 10

class Nokia:
    def __init__(self, battery:Battery, color:str='черный') -> None:
        self.color = color
        self.battery = battery
    def spend_power(self):
        self.battery._power -= 10

iphone = Iphone('розовый')
del iphone
battery = Battery()
nokia = Nokia(battery, 'синий')
del nokia


class Wheel:
    pass

class Car:
    def __init__(self, wheels, color) -> None:
        self.wheels = wheels
        self.color = color

wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
car = Car(wheels, 'оранжевый')
del car

# написать класс Printer и Document
# создать связь(композицию) между этими классами

class Printer:
    def print_document(self, document):
        print('skan')
        content = document.content
        print(content)

class Document:
    def __init__(self, content) -> None:
        self.content = content
        self.printer = Printer()
    def print_content(self):
        self.printer.print_document(self)

document = Document('content')
# docment.printer
document.print_content()
# написать метод print_document, который принимает документ
# сканирует документ
# вытаскивает контент
# выводит в терминал контент

# написать два класса Course и Student
# создать связь(агрегацию) между этими классами

# класс Course: 
    # students = []
    # name = 'math'

    # def add_student(self, student:Student)

# класс Student:
    # name
    # student_id
class Student:
    def __init__(self, name, student_id) -> None:
        self.name = name
        self.id = student_id
    
    def __str__(self) -> str:
        return self.name

class Course:
    def __init__(self, title) -> None:
        self.title = title
        self.students = []

    def add_student(self, student:Student):
        self.students.append(student)
    
    def get_students(self):
        for student in self.students:
            print(student.name)
    def __str__(self) -> str:
        return f'{self.students}'

math_course = Course('math')
nikita = Student('Nikita', 1)
math_course.add_student(nikita)
# print(math_course.get_students())