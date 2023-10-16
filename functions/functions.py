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


"===========Виды аргументов==========="
# 1. - позиционные
# 2. - именованные

def func(a, b=5, *args):
    return a*b
print(func(1,2,3))
func(a=5, b=435)
number1 = 6
number2 = 7
func(number1, number2) # 42
func(b=5, a=435)
# func(a=5, 4) # SyntaxError: 
func(4, b=5)

# надо написать функцию которая принимает строку
# и возвращает перевернутую строку
# hello
# olleh

def reverse(string:str)->str:
    return string[::-1]
string = reverse('hello') # olleh
print(string) # olleh


def func():
    print(5)
    return func
func()()()()()()()()()


# 'руддщ' - 'hello'
# 'hello' - 'руддщ'

def translate(string:str):
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    arab = "ضصثقفغعهخحجدشسيبلاتنمكطئءؤرلاىةز"
    if string[0] in eng:
        dict_ = ''.maketrans(eng, arab)
    else:
        dict_ = ''.maketrans(arab, eng)
    return string.translate(dict_)
print(translate('غخعفعلث'))

# надо написаит функцию is_palindrome
# которая принимает строку
# mom, dad, tenet
# надо вернуть True если слово палиндромное
# False если слово не палиндромное

def is_palindrome(string:str)->bool:
    if string[::-1].lower() == string.lower():
        return True
    else:
        return False
print(is_palindrome('MpPm')) # True

рекурсия - ДЗ

"===========Анонимная функция==========="
# lambda - анонимная функция, которая записывается в одну строчку
func = lambda x:x**2
print(func(2)) # 4

# с помощью функций написать калькулятор
# plus, minus, mul, div

def plus(a1, a2):
    return a1+a2
def minus(a1, a2):
    return a1-a2
def mul(a1, a2):
    return a1*a2
def div(a1, a2):
    return a1//a2



# calc = {
#     '+':plus(num1, num2),
#     '-':minus(num1, num2),
#     '*':mul(num1, num2),
#     '//':div(num1, num2),
# }
calc = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '//': lambda x,y: x//y
}
def main():
    try:
        num1 = int(input('num1: '))
        num2 = int(input('num2: '))
        operation = input('operation choice(+|-|*|//): ')

        func = calc[operation]
        print(func(num1, num2))
    except ValueError:
        print('Введите число!!!')
    except KeyError:
        print('Неизвестный оператор')
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')
    finally:
        print('До скорой встречи!')

while True:
    main()
    answer = input('завершить? (y/n)')
    if answer.lower() == 'y':
        break

