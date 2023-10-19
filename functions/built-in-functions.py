"============Встроенные функции============"

# print(dir(__builtins__)) # [встроенные функции]
# print, input, list, sorted, sum, len, abs, isinstance, type

# map, filter, zip, reduce, enumarate

# zip - соединяет несколько последовательностей
list1 = [1,2,3,4]
list2 = ['a', 'b', 'c', 'd']
list3 = [10.5, 11.5, 12.5, 13.5]
print(list(zip(list1, list2, list3)))
(1, 'a', 10.5)

print(dict(zip(list1, list2))) # {1:'a', 2:'b', ...}

list1 = [[1], [2], [3], [4]]
list2 = ['a', 'b', 'c', 'd']
new_dict = dict(zip(list1, list2)) # TypeError
print(new_dict) 

# enumerate - нумерует последовательность (по умолчанию с 0)
list1 = ['a', 'b', 'c', 'd']

dict_ = {'a':1, 'b':2}
print(dict_.items()) # ('a', 1)

new_list = list(enumerate(list1, start=0))
[(0, 'a'), (1, 'b'), ...]
for i, val in new_list:
    print(i,'index', val, 'value')

# map - принимает функцию и последовательность (записывает в новую последовательность результат функции)

list1 = ['1', '2', '3', '4']
# list1 = [int(i) for i in list1]
list1 = list(map(int, list1))
# list1 = [i**2 for i in list1]
list1 = list(map(lambda x: x**2, list1))
print(list1)

# filter - принимает функцию и последовательность фильтрует по тому что возвращает функция (если True - оставляет | если False - убирает)

list1 = [-1, -2, 0, 1, 12, -0.5]
def func(x):
    return x > 0
list1 = [i for i in list1 if i > 0]
list1 = list(filter(lambda x: x>0, list1))
print(list1)

# reduce - принимает функцию с двумя аргументами и последовательность возвращает результат полученный из двух аргументов
from functools import reduce

list1 = [1,2,4,5,6]
def func(x, y):
    print(x, y)
    return x+y
# list1 = reduce(func, list1)
# list1 = reduce(lambda x, y: x+y, list1)
# print(list1) # 18
def func(x,y):
    # print(x, y)
    if x>y:
        return x
    else:
        return y
list1 = reduce(func, list1)
# list1 = reduce(lambda x, y: x if x>y else y, list1)
print(list1)


# itertools
# collections
# YAGNI

# all any sorted 