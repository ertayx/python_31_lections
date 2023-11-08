# Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать в дочернем классе все методы и аттрибуты родительского класса

# object - класс прородитель в котором хранятся все маг.методы

# class A:
#     h = 5
#     def method(self):
#         print('method A')

# class B:
#     h = 0
#     def method(self):
#         print('method B')
# class C(B, A):
#     pass

# c = C()
# c.method()

# b = A()
# b.method()
# b.h
# print(dir(B))

class Human:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex
    
    def get_info(self):
        return f'My name is {self.name}, I`m {self.age} y.o'

class Student(Human):
    def __init__(self, name, age, sex, facultet, kurs) -> None:
        super().__init__(name, age, sex)
        self.facultet = facultet
        self.kurs = kurs
        # super(Student, self).get_info
    
    def get_info(self):
        return super().get_info() + f', I`m studying at {self.facultet} on {self.kurs} course'
    
student1 = Student('Nikita', 20, 'Male', 'IT', 3)
# print(student1.get_info())
# print(super(Student, student1).get_info())

# одиночное наследование
# множетсвенное наследование
# многоуровневое наследование
# иерархическое наследование
# гибридное наследование

# class A:
#     pass
# class B:
#     pass
# class C(A, B):
#     pass
# class D(A, B):
#     pass
# class E(C, D):
#     pass

# print(E.mro())
# [<class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

class A:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name + 'str'
    
    def __repr__(self) -> str:
        return self.name + 'repr'

a = A('Tima')
print(a)

# __str__ | __repr__
# len
# yield

class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)
a = IterInt(123456789)

