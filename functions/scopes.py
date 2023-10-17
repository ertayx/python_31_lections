"============Области видимости============"
# LEGB - local enclosed global build-in

"============Build-in============"
# встроенное пространсвто имен - (print, input, max, min)
# a = 5
# print(dir(__builtins__))

"=============Global============="
# пространсвто имен в котором хранятся все глобальные переменные, которые мы обьявили внутри этого файла
# что бы посмотреть все глобальные переменные, можно использовать globals

# def func():
#     pass
# b = 7
# n = 8
# print(globals())

"===========Enclosed==========="
# замкнутое пространство имен - локальное пространство у которого есть внутренне локальное пространство

var = 'глобальная переменная'
print(var)
def func():
    var = 'замкнутая переменная'
    print(var)
    def inner_func():
        var = 'локальная переменная'
        print(var)
    inner_func()
func()
# global enclosed local

"===============Local==============="
# локальное пространство имен - переменные, созданные внутри функции

# a = 10
# def func(a,b):
#     # print('GLOBAL', globals()) # {a:10, func:<link>}
#     print(a) # 5
#     n = 8
#     def inner_func(a,b):
#         pass
#     inner_func(6,7)
#     print('LOCAL', locals()) # {a:5, b:7,n:8, inner_func:<link>}
# func(5,7)

# count = 0
# def counter():
#     global count
#     count+=1
#     print(count)
# counter() # 1
# counter() # 2
# counter() # 3
# counter() # 4

# a = 8

# def count():
#     counter = 0

#     def inner_count():
#         nonlocal counter
#         global a
#         a+=10
#         counter+=1
#         print(counter)
#     inner_count()
#     return counter

# print(count())
# print(a)

# print(locals()) # 
# def func(a):
#     print(locals())
# func(3)

# a = 7
# def func():
#     global a
#     a+=1

# python ищет переменную - по принципу LEGB