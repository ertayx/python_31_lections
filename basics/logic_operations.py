"=============Логические и условные операторы==========="
# логические операторы - выражения, которые возвращают True, если выражение верное, False - если не верное

# равенство
5==5 # True
4==5 # False

# не равенство
4!=5 # True
5!=5 # False

# больше
5>4 # True
4>5 # False
5>5 # False

# меньше
5<4 # False
5<10 # True
5<5 # False

# больше или равно
5>=10 # False
10>=5 # True
5>=5 # True

# меньше или равно
10<=5 # False
5<=10 # True
5<=5 # True

'5'=='5' # True
'5'==5 # False
'hello'=='hello' # True
'Hello'=='hello' # False

"==============And Or Not============="
# and - и
# or - или
# not - не

a = 5
b = 6

# True and True
a == 5 and b == 6 # True
# True and False
a == 5 and b == 7 # False
# False and False
a == 4 and b == 4 # False

a == 5 or b == 6 # True
a == 5 or b == 7 # True
a == 4 or b == 4 # False

not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a != 4)

# is | ==

not 5==5 and 6==6 # False
not 5==5 and 7==0 # True
not 7>=5 or 6<=4 # False
not not not True # False

"============Boolean Type=========="
# Булевый тип данных имеет всего 2 значения True и False

bool(1) # True
bool(0) # False
bool(-22) # True

bool('') # False
bool(' ') # True
bool('hell') # True

bool(True) # True
bool(False) # False
bool('False') # True

bool([]) # False
bool([[]]) # True

"=============None Type=========="
# None - неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения

bool(None) # False
bool('None') # True

a = None
a == None # True

'hello world' == 'hello' # False
'hello' in 'hello world' # True
# print('hello' >= 'hellw') # False 

"=============Условные операторы==========="
# условные операторы - конструкция, которая испоьзуется для того, чтобы при разных входных данных код работал по разному (в зависимости от условия)

# if условие:
#     тело
#     # тело будет выполнятся если условие верное
# if условие:
#     тело
#     # тело будет выполнятся если условие верное
# else:
#     тело2
#     # тело2 будет выполнятся во всех других случаях
# if условие1:
#     тело1
#     # тело1 будет выполнятся если условие1 верное
# elif условие2:
#     тело2
#     # тело2 будет выполнятся если условие1 не верное и если условие2 верное
# else:
#     тело3
#     # тело3 будет выполнятся только если все вышеуказанные условия не верные

# надо принять от пользователя число если число отрицательное то ваша программа должна вывести в терминал сообщение 'NEGATIVE', а если число положительное то 'POSITIVE', а если ноль то программа выводит 'ZERO'

# num = int(input('Введите число: '))

# if num < 0:
#     print('NEGATIVE')
# elif num == 0:
#     print('ZERO')
# else:
#     print('POSITIVE')

# username = 'nikita'
# password = '123456'

# input_username = input('Введите ваш username: ')
# input_password = input('Введите ваш password: ')

# if input_username.lower() == username.lower() and input_password == password:
#     print('yes')
# else:
#     print('no')

"=============Тернарные операторы============"
# тернарные операторы - условие в одну строчку
# тело1 if условие else тело2

# принять от пользователя число если число равняется 5 то выводим hello, в ином случаи выводим bye

# num = int(input('Введите число: '))
# print('hello') if num == 5 else print('bye') 
"""этот код предназначен для принятия и сравнения числа с 5 """
# if num == 5:print('hello') else print('bye')

# if num == 5:
#     print('hello')
# else:
#     print('bye')

# примите число от пользователя
# выведите Fizz, если число кратно 3
# выведите Buzz, если число кратно 5
# выведите FizzBuzz, если число кратно и 3, и 5
# выведите число во всех остальных случаях

num = int(input('Введите число: '))
if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%5==0:
    print('Buzz')
elif num%3==0:
    print('Fizz')
else:
    print(num)