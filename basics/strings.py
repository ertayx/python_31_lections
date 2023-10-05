"============Строки==========="
# строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки

string = 'Dont Hello" World'
string1 = "Hello World"
string2 = "Don't" # внутри двойных кавычек все одинарные - просто символы
string3 = ' "     '  # внутри одинарных все двойные - просто символы

''' Don't  "Hello" '''
""" Don't  "Hello" """

# print('asdf' + '2') # asdf2 
# print('asdf' * 2) # asdfasdf

string = 'Hello'
string2 = 'World'
# print(string+' '+string2) # Hello World
# print(string / 2) # Error

# Конкатенация - склеивание строк

"===========Экранизация строк=========="
'\n' # перенос на новую строку
# print('hello\nworld')
#hello
#world

'\t' # табуляция
# print('hello\n\tworld') # hello   world
# hello
#   world

# print('Don\'t') 
# print("Dont\"t")
# print("hello \\nero")
# hello nero

'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки
# print('hello\vworld\vmakers\vbootcamp')
# hello
#      world
#           makers
#                 bootcamp

"=============Форматирование строк============"
title = 'plov'
price = 201
print(f'название: {title}\nцена: {price}')
# название: manty
# цена: 201

# надо принять с терминала название блюда и вывести такое сообщение:
# название блюда был вкусный

# title = input('Введите название блюда: ')
# print(f'{title} был вкусный')

format2 = 'Название: {}\nЦена: {}'
print(format2.format(title, price)) # старый способ
# Название: plov
# Цена: 201

format3 = 'Название: %s\nЦена: %s'
print(format3 % (title, price)) # старый способ

"=============Методы строк============"
# методы - функции, которая относится к определенному классу (типу данных), к ним мы обращаемся чз точку

print(dir(str))

'HELLO'.lower() # hello
'hello'.upper() # HELLO

'HEllO'.swapcase() # heLLo
'hello world'.capitalize() # Hello world
'hello world'.title() # Hello World

'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello world'.count('oo') # 0

'hello world'.startswith('hello') # True
'hello world'.startswith('Hello') # False
'hello world'.endswith('ld') # True

'hello world'.islower() # True
'HELLO'.isupper() # True
'1234'.isdigit() # True
'hello !'.isalpha() # True
'hello !'.isalnum() # False
'1234 '.isalnum() # False
'h1'.isalnum() # True

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell', ' w', 'rld']
'hello world'.split('makers') # ['hello world']

'1'.join(['hello', 'world', 'rt']) # 'hello1world1rt'
'hello'+'1'+'world'+'1'+'rt'

string = '                    hello world          '
print(string.strip()) # 'hello world'
print(string.lstrip()) # 'hello world          '
print(string.rstrip()) # '                    hello world'

string = '$$as$df$$$$'
string.strip('$') # as$df

string = '$$as$df$$$$'
string.replace('$', '') # asdf
string.replace('$', '', 2) # as$df$$$$


"==============Индексы=============="
# индекс - порядковый номер элемента в последовательности (символ в строке) (индексация начинается с 0)

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#            ...-3 -2 -1

string = 'hello world'
string[2] # 'l'
string[0] # 'h'
string[6] # 'w'
string[10] # 'd'
string[-1] # 'd'

# срез - подстрока строки
string[0:5] # hello
string[0:4] # hell
string[6:10] # worl
string[6:-1] # worl
string[6:]  # world
string[:5] # hello
string[:] # hello world

string[:2] + string[-2:]# he + ld = held

'hello world'
string[::2] # hlowrd
string[1:5] # ello
string[1:5:2] # el
string[::-1] # dlrow olleh
string[::-2] # drwolh
string[::3] # hlwl

# question isnumeric|isdigit|isdecimal ?

immutable_string = 'hello'
immutable_string = immutable_string.upper() #HELLO
immutable_string = immutable_string[::-1] #OLLEH
print(immutable_string) # OLLEH

string = 'world'
string[:-3] # wo
print(string) # world

# s3 = "½"
# s3 = "Ⅳ"
# print(s3.isdigit())
# print(s3.isnumeric())
# print(s3.isdecimal())