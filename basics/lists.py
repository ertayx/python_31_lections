"===============Список============="
# список - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list1 = [1, 2, 3, 'hello', [2, 0, 0.2], None, True, False]
list1[3] # hello
list1[3][-1] # o
list1[-1] # False
list1[4] # [2, 0, 0.2]
list1[4][1] # 0

list2 = list("hello")
['h', 'e', 'l', 'l', 'o']

list3 = list(range(1, 11))
print(list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list4 = [1] * 5
# [1,1,1,1,1]

"============Методы списков==========="
# append - добавляет элемент в конец списка
list1 = []
list1.append(1)
# print(list1) # [1]
list1.append('hello')
# print(list1) # [1, 'hello']
list1.append([1,2,3]) # [1, 'hello', [1,2,3]]

# pop - удаляет элемент из списка по индексу и результатом метода будет удаленный элемент (метод возвращает удаленный элемент), если не передать индекс - удалит с конца
list1 = [1,2,'hello',4,5,6]
popped = list1.pop(2)
list1.pop()
# print(list1, popped) # [1, 2, 4, 5] 'hello'

# если список пустой, то при удалении выйдет IndexError
# list1 = []
# list1.pop()
# IndexError

# remove - удаляет по значению (первый найденный элемент)
list1 = [1,2,'hello',4,5,6]
removed = list1.remove('hello')
# print(list1, removed) # [1, 2, 4, 5, 6] None

list1 = [1] * 4
list1.remove(1)
# print(list1) # [1, 1, 1]

# count - считает количество принятого элемента в списке
list1 = [1, 1, 1, 1, 2, 3, 4, 5, 5]
list1.count(1) # 4

list1 = ['hello', 'hello', 'hello']
list1.count('hello') # 3
list1.count('l') # 0

# insert - добаляет элемент в список по индексу
# list1 = [1,2,3,4,5,6]
# list1.insert(0, 'hello')
# print(list1) # ['hello', 1, 2, 3, 4, 5, 6]

# extend - добавляет элементы принятого распакуемого обьекта в список
list1 = [1,2,3]
list1.append([4,5,6]) # [1,2,3,[4,5,6]]
list1.extend([4,5,6]) # [1,2,3,4,5,6]
list1.extend('hello') # [1,2,3,'h','e','l','l','o']

# reverse - переворачивает список
# list1 = [1,2,3]
# list1.reverse()
# print(list1) # [3,2,1]

# sort - сортирует список, состоящий из элемнтов одного типа данных
# list1 = [3,2,1,5,4,1]
# list1.sort()
# print(list1) # [1,1,2,3,4,5]

# list1 = ['b', 'a', 'c']
# list1.sort()
# print(list1) # ['a', 'b', 'c']

list1 = ['a', 1, 2, 3]
list1.sort()
print(list1) # TypeError

"==============For============"
# цикл - блок кода который отрабатывает несколько раз

list1 = [1,2,3]
for number in list1:
    print(number)

number = list1[0]
print(number)
number = list1[1]
print(number)
number = list1[2]
print(number)

# надо создать диапазон чисел от 1 до 255, если число четное то мы добавляем в новый список четное число а если число не четное то мы выводим такой текст: "чача мачача". в конце мы должны вывести список с четными числами

given_list = list(range(1,11))
new_list = []
for num in given_list:
    if num % 2 == 0:
        new_list.append(num)
    else:
        print('чача мачача')
print(new_list)