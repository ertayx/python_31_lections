"==============Функции=============="
# функция - именованный блок кода, который может принимать аргументы и возвращать результат

def func(x:int, y:int, c:int) -> int: # параметры
    """
    this function return x + y
    """
    return x+y # возвращаю результат
# print(func(5,5,6)) # аргументы
a = func(1,1,1)

def mul(x:int,y:int,z:int)-> int:
    """
    multiply x,y,z
    """
    return x*y*z
result = mul(2,3,1)
# print(result)
# print(['1'].append('2')) # None

# написать функцию my_len которая принимает строку 
# и возвращает длину этой строки

def my_len(string:str):
    counter = 0
    for i in string:
        counter+=1
    return counter
print(my_len('hello')) # 5

def func():
    try:
        return 0
    finally:
        return 1
print(func()) # 1 
# return value = None
# return value = 0
# return value = 1

# DRY - don't repeat yourself

"=============Аргументы и параметры============="
# парамаетры - переменные внутри функции, значения которые мы задаем при вызове функции (рецепт пиццы)
# аргументы - значения, которые мы передаем при вызове функции (ингредиенты пиццы)

"============Виды параметров============"
# 1.обязательные
# 2.не обязательные
# 2.1. с дефолтом (по умолчанию)
# 2.2. args (все позицонные аргументы)
# 2.3. kwargs (все именованные аргументы)

def func(a, b=3, *args, **kwargs):
    print(args) # (3,2,4)
    print(kwargs) # {'c':3}
    return a + b
print(func(b=4, a=5, c=3))
# print(1,2,3,4,5,6,sep='assa')