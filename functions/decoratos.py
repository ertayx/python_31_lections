"===========Декораторы==========="
# декоратор - функция высшего порядка, которая нужна чтобы расширять функционал функции не изменяя ее (функция обертка)

# DRY
def decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__} отработала за {end-start}')
    return wrapper

@decorator
def func():
    a = []
    for i in range(1,1000000):
        a.append(i)
    return a
print(func()) 

def func2():
    a = [i for i in range(1,1000000)]
    return a

result = decorator(func2)
result()

# 1. decorator
# 2. wrapper
# 3. function

def get_year(func):
    def wrapper(*args, **kwargs):
        print(f'{func(*args)}. Вы родились в {2023 - args[-1]}')
    return wrapper

def get_info(name, last_name, age):
    return f"Ваше имя {name}, ваша фамилия {last_name} ваш возраст {age}"
result = get_year(get_info)
result('John', 'Snow', 72)

# с помощью декораторов вывести год рождения пользователя

# @bread - добавляет хлеб с двух сторон начинки
# "хлеб сосиска хлеб"
# @ingredients - добавляет помидор и салат с двух сторон начинки
# "помидор сосиска салат"

def bread(func):
    def wrapper_bread(*args, **kwargs):
        return 'хлеб ' + str(func(*args)) + ' хлеб'
    return wrapper_bread

def ingredients(func):
    def wrapper_ingredients(*args, **kwargs):
        return 'помидор ' + str(func(*args)) + ' салат'
    return wrapper_ingredients
@bread
@ingredients
def get_sandwich(x):
    return x
get_sandwich('сосиска')

result = bread(ingredients(get_sandwich))
result('сосиска')

# 1. ingredients(get_sandwich) - wrapper_ingredients
# 2. bread(wrapper_ingredients) - wrapper_bread
# 3. result(сосиска) 
# 3. wrapper_bread(wrapper_ingredients)
# 4. wrapper_ingredients(get_sandwich)
"хлеб помидор сосиска салат хлеб"