"================Циклы=============="
# цикл - это блок кода, который отрабатывает несколько раз
# for - цикл, который работает с итерируемыми обьектами, цикл заканчивыает работу после перебора всех занчений итерируемого обьекта
# while - цикл, который работает до тех пор пока условие верное

# while True:
#     print('hello')
    # будет работать бесконечно

# num_1 = int(input('введи первое число: '))
# num_2 = int(input('введи второе число: '))
# operation = input('выбери операцию "+, *, /, -": ')

# if operation == '+':
#     print(num_1+num_2)
# elif operation == '-':
#     print(num_1-num_2)
# elif operation == '*':
#     print(num_1*num_2)
# elif operation == '/':
#     print(num_1/num_2)
# else:
#     print('такой операции нет!!!')


# play = True

# while play:
#     num_1 = int(input('введи первое число: '))
#     num_2 = int(input('введи второе число: '))
#     operation = input('выбери операцию "+, *, /, -": ')

#     if operation == '+':
#         print(num_1+num_2)
#     elif operation == '-':
#         print(num_1-num_2)
#     elif operation == '*':
#         print(num_1*num_2)
#     elif operation == '/':
#         print(num_1/num_2)
#     else:
#         print('такой операции нет!!!')
    
#     one_time = input('хотите продолжить? yes/no: ')

#     if one_time.lower() == 'yes':
#         play = True
#     elif one_time.lower() == 'no':
#         play = False
#         print('еще увидимся')
#     else:
#         print('попробуй еще!!!')
    


# break, continue

# break - прерывает цикл
# continue - пропускает итерацию (пропускает один цикл)

# string = 'hello world'

# for i in string:
#     if i != 'o':
#         continue
#     print(i*2)
# oo
# oo

# nums = list(range(1,101))
# nums2 = []
# for x in nums:
#     if x%2 == 0:
#         continue
#     nums2.append(str(x)+f'{x}')
# print(nums2)
# ['11', '33', '55']



mary = [
    {
        'name': 'Nikita',
        'password': '1234567'
    },
    {
        'name': 'Ivan',
        'password': '563'
    },
    {
        'name': 'Bagyshan',
        'password': '0404'
    },
    {
        'name': 'Jalyn',
        'password': '115'
    },
    {
        'name': 'Amir',
        'password': '100'
    },
    {
        'name': 'Bilal',
        'password': '008'
    },
    {
        'name': 'Abdugadi',
        'password': '777'
    },
    {
        'name': 'Aitenir',
        'password': '007'
    },
    {
        'name': 'Ramazan',
        'password': 'sweden_976'
    },
    {
        'name': 'Almaz',
        'password': '1'
    },
    {
        'name': 'Adilet',
        'password': '666'
    },
    {
        'name': 'Erlan',
        'password': '555'
    },
    {
        'name': 'Meder',
        'password': 'net parolya'
    },
    {
        'name': 'Denis',
        'password': '13'
    },
    {
        'name': 'Argen',
        'password': 'sudo'
    },
    {
        'name': 'Sam',
        'password': '-1'
    },
    {
        'name': 'Aymash',
        'password': '506'
    },
    {
        'name': 'Sagida',
        'password': 'osh_3000'
    },
    {
        'name': 'Begimay',
        'password': 'python3'
    },
    {
        'name': 'Alina',
        'password': '126'
    },
    {
        'name': 'Eraaly',
        'password': '1000-7'
    },
    {
        'name': 'Ayganysh',
        'password': 'chachamacha24'
    },
    {
        'name': 'Ertay',
        'password': 'python31makers'
    },
    {
        'name': 'Timurlan',
        'password': 'nomad'
    },
    {
        'name': 'Ademi',
        'password': '2002'
    },
    ]

play = True
while play:
    name = input('Enter your name: ')
    password = input('Enter your password: ')

    user_found = False

    for user in mary:
        if user['name'].lower() == name.lower() and user['password'] == password:
            print('Login successful!')
            user_found = True
            break

    if not user_found:
        print('User not found or incorrect password.')

    one_more_time = input('Do you want to continue? (yes/no): ')

    if one_more_time.lower() == 'yes':
        play = True
    elif one_more_time.lower() == 'no':
        play = False
        print('Goodbye!')
    else:
        print('Invalid input. Please try again.')