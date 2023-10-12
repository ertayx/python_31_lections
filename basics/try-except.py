"===============Exceptions==========="
# Исключения (ошибки) - обьекты, которые прерывают работу кода, если не были обработаны

SyntaxError
# исключение, которое выходит, когда в коде допущена синтаксическая ошибка
""" 
print(
# SyntaxError: unexpected EOF while parsing
(когда мы не закрыли скобочку или кавычку)
"""

"""
a = 
SyntaxError: invalid syntax
(когда мы сделали что то не то в синтаксисе)
"""

NameError
# исключение, которое выходит, когда мы обращаемя к несуществующей переменной
"""
name.split()
NameError: name 'name' is not defined
"""

TypeError
# исключение, которое выходит, когда мы проводим не правильные операции между типами данных
""" 
'asdf' + 2
TypeError: can only concatenate str (not "int") to str 
"""
"""
{1,2,3, [1,2,3]}
TypeError: unhashable type: 'list'
"""
"""
for i in 12345678:
    pass
TypeError: 'int' object is not iterable
"""

"""
input('введи возраст', 1) 
TypeError: input expected at most 1 argument, got 2
"""
"""
[].append()
TypeError: append() takes exactly one argument (0 given)
"""
IndexError
# выходит когда, указали не существующий индекс
list_ = [1,2,3,5,6,7]
"""
list_[27]
IndexError: list index out of range
"""
"""
list_.pop(1000)
IndexError: pop index out of range
"""

KeyError
# выходит когда мы передали не существующий ключ

"""
dict_ = {'a':6}
dict_['b']
KeyError: 'b'
"""

dict_ = {'a':6}
dict_['b'] = 7
print(dict_.clear())
dict_.get('a')
print(dict_)

ValueError
# выходит когда мы передаем не правильный тип данных в определенную функию
"""
int('asdf')
ValueError: invalid literal for int() with base 10: 'asdf'
"""
"""
a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)
"""
list_ = [1,2]
a = list_[0]
b = list_[1]
a,b = list_

ZeroDivisionError
# выходит при делении на 0
"""
45 / 0

45 // 0

45 % 0
"""
AttributeError
# выходит когда мы обращаемся к не существующему методу обьекта (типу данных)
"""
list_ = [1,2,3]
list_.replace(1, 'hello')
print(list_) ['hello', 2, 3]
"""
"""
string = 'hello'
string.pop(0)
print(string)
"""
IndentationError
# выходит когда мы не правильно используем отступы
"""
 a = 5
"""
"""
for i in [1,2,3]:
print(i)
"""

Exception
# исключение, которое создали, что бы его вызвать

"============Вызов исключений============"

# raise Exception()

# raise NameError('я хочу что бы эта вышла')

"============Обработка исключений==========="
# чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обрабатывать исключения

# try:
#     age = int(input('Введи свой возраст'))
# except Exception as e:
#     print('введи число', type(e))

# надо принять от пользователя два числа 
# и разделить их друг на друга
# надо обработать ошибки которые могут возникнуть
# при отработке кода

'введи число'
'нельзя делить на ноль'

# try:
#     num1 = int(input('num1: '))
#     num2 = int(input('num2: '))
#     num1 // num2
# except ValueError:
#     print('введи число')
# except ZeroDivisionError:
#     print('нельзя делить на ноль')


# try:
#     num1 = int(input('num1: '))
#     num2 = int(input('num2: '))
#     num1 // num2
# except Exception as e:
#     if type(e) == ValueError:
#         print('введи число')
#     elif type(e) == ZeroDivisionError:
#         print('нельзя делить на ноль')
#     else:
#         print(e)

try:
    age = int(input('Введите свой возраст: '))
    if age == 7:
        raise Exception('вам вход в клуб запрещен')
    # код, который возможно вызовет ошибку
except ValueError:
    # код, который отработает когда выйдет ошибка
    print('введи число')
except Exception:
    print('вам вход в клуб запрещен')
else:
    # код, который отработает только если никакая ошибка не вышла
    print('введенное число', age)
finally:
    # код, который отработает вообще в любом случае
    print('до свидания')


# ичключения - мы можем словить (косяк со стороны клиента)
# ошибка - мы не можем словить (косяк со стороны разработчика)

KeyboardInterrupt # за что отвечает эта исключение