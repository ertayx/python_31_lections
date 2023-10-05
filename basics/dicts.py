"==============Словари============="
# dict - изменяемый, итерируемый, неидексируемый, неупорядоченный тип данных, где данные хранятся в парах (ключ:значение)

user = {
    'name':'Ertay',
    'password': '12345678',
    'last_name': 'Esenbekov'
    }
print(user['password']) # 12345678

# ключами в словаре могут быть только не изменяемые типы данных

dict1 = {'a':{'a':'b'}, 'b':1, 'a':5, 'a':6}
print(dict1['a']) # 6
# если ключи одинаковые, сохраняется только последнее занчение

# print(dict1['c']) # KeyError: 'c'

"===============Создание============"
dict1 = {'a':'hello'}
dict1 = dict([('a','hello')]) # {'a':'hello'}
dict2 = dict(["ab", "cd"]) # {'a':'b', 'c':'d'}
# print(dict1)
dict1 = {}
dict1['name'] = 'Ertay'
# {'name':'Ertay'}
dict1['name'] = 'Tima'
# {'name':'Tima'}
"KISS" # keep it simple, stupid

"===============Методы словаря============="
# get - метод, который возращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение
user = {
    'name':'Ertay',
    'password': '12345678',
    'last_name': 'Esenbekov'
    }
# print(user['nam']) # KeyError
print(user.get('nam', 'yes')) # yes

# pop - удаляет пару по ключу и возвращает значение
dict1 = {'a':1, 'b':2}
popped = dict1.pop('a')
print(dict1, popped) # {'b':2} 1
del dict1['b'] # {}

# popitem - удаляет последюю пару и возвращает ее
dict1 = {'a':1, 'b':2}
popped = dict1.popitem()
print(dict1, popped) # {'a':1} ('b', 2)

# update - добавляет новую пару, если есть существующая пара, то он заменяет ее
dict1 = {1:'a', 2:'b', 3:'c'}
dict1[4] = 'd' # {1:'a', 2:'b', 3:'c', 4:'d'}
dict1.update({4:'e'}) # {1:'a', 2:'b', 3:'c', 4:'e'}
print(dict1)

# clear - очищает словарь
dict1 = {1:'a', 2:'b', 3:'c'}
dict1.clear()
print(dict1) # {}

# keys - возвращает все ключи
# values - возвращает все значения
# items - возвращает все пары (ключ, значение)

user = {
    'name':'Ertay',
    'password': '12345678',
    'last_name': 'Esenbekov'
    }
print(user.keys()) # dict_keys(['name', 'password', 'last_name'])
print(user.values()) # dict_values(['Ertay', '12345678', 'Esenbekov'])
print(user.items()) # dict_items([('name', 'Ertay'), ('password', '12345678'), ('last_name', 'Esenbekov')])

"================Итерирование словарей=============="
user = {
    'name':'Ertay',
    'password': '12345678',
    'last_name': 'Esenbekov'
    }
for key in user:
    print(key)
    # при итерации словаря будут только ключи
for value in user.values():
    print(value)
    # при итерации dict_values будут приходить значения
for key, value in user.items():
    print(key, value)
    # при итерации dict_items будут приходить и ключи и значения в виде tuple

item = ('name', 'Ertay')
key, values = ('name', 'Ertay')

# вам дан словарь
{'a':1, 'b':2, 'c':3}
# создайте новый словарь в котором надо поменять местами ключ и значение
# {1:'a',2:'b',3:'c'}

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {}
for key, value in dict1.items():
    dict2.update({value:key})
print(dict2) # {1:'a',2:'b',3:'c'}