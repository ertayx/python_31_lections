"============JSON============"
# JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных для многив языков программирования
{
    "name":"asdf"
}
import json

# ==========DUMP DUMPS
# сериализация - перевод в формат JSON
# DUMPS - переводит данные в json (str)
# DUMP - принимает в себя данные и файл чтобы записать эти данные в наш файл
list_ = [1,2,3,4,5]
data = {
    'name':[1,2,3,4],
    'last_name':'Grebnev'
}
# print(type(list_)) # list
# list_ = json.dumps(list_)
# print(type(list_)) # str
# # записать в файлик data.json список
# file = open('data.json', 'w')
# json.dump(data, file)
# file.close()

# ==========LOAD LOADS
# десериализация - перевод с json в python
# loads - переводит данные с json в python
# load - принимает файл и переводит этот файл в python
with open('data.json', 'r') as file:
    data = json.load(file)
    print(type(data))
    # data = file.read()
    # print(type(data)) # str
    # data = json.loads(data)
    # data = eval(data)
    # print(type(data))
    # print(type(data)) # dict

# CSV