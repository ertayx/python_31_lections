"=============Модули и пакеты============="
# модуль - любой файл с расширением .py
# пакет - набор модулей (обязательно должен быть файл __init__.py)

# import math -> модуль
# import random -> модуль
# import itertools -> модуль


"============Работа с файлами============"
# file = open('test.txt', )
# print(file.read())
# open - функция, которая открывает файл, в определенном режиме

# r - read (только для чтения) 
# w - write (только для записи)
# a - append (только для дозаписи, добавляет в конец)
# x - создает файл, но если существует такой файл выдаст ошибку
# b - binary (в бинарном виде)

# ============READ
try:
    file = open('test.txt', 'r')
    print(dir(file))
    print(file.readable()) # True
    print(file.writable()) # False
    print(file.read())
    print(file.tell())
    file.seek(1000)
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readlines())
    print(file.tell())
finally:
    file.close()

# ========WRITE
try:
    file = open('test.txt', 'w')
    file.write('my name is Anton\n')
    # file.seek(17)
    file.write('my name is Anton\n')
    # file.writelines(['Makers\n', 'bootcapm\n'])
    file.write('ggg hhh www')
finally:
    file.close()

# ========APPEND
try:
    file = open('test.txt', 'a')
    file.write('\nhello')
    file.seek(0)
    file.write('i am John\n')
finally:
    file.close()

"============Контекстный менеджер============"

with open('test.txt', 'r') as file:
    print(file.read())

with open('test.txt', 'a') as file:
    # print(dir(file))
    file.write('hello\n')

with open('ertay.py', 'x') as file:
    if file.writable():
        file.write('print("hello world")')

class Test:
    def __enter__(self):
        print('начало работы')
        return self

    def __exit__(self, *a, **kw):
        print('завершение работы')
        return self

    def hello(self):
        print('Hello world')

with Test() as test:
    test.hello()