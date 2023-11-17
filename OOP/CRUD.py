import re
{1:['username', '...'], 2:[]}

class RegisterUserMixin:
    id = 1
    def register(self, username, email, password, password_confirm) -> None:
        self.id = RegisterUserMixin.id
        RegisterUserMixin.id+=1
        self.username = username
        self.email = email
        self.password = password
        self.password_confirm = password_confirm
        self._validate_password()
        self._validate_email()
        self.database.update({self.id:[username, email, password]})
    
    def _validate_password(self):
        symbols = '!@#$%^&*_+-~`'
        if not self.password == self.password_confirm:
            raise Exception('Пароли не совпадают')

        if len(self.password) <= 8:
            raise Exception('длина пароля должна превышать 8 символов')
        if not any(i.isalpha() for i in self.password):
            raise Exception('Пароль дожен состоять из букв')
        elif not any(i.isdigit() for i in self.password):
            raise Exception('Пароль дожен состоять из цифр')
        elif not any(i in symbols for i in self.password):
            raise Exception('Пароль дожен состоять из символов')
    
    def _validate_email(self):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', self.email):
            raise Exception('не правильная почта')
        for v in self.database.values():
            if self.email in v:
                raise Exception('такая почта уже существует')
        
# regex
# regular expressions
# регулярные выражения

class LoginUserMixin:
    def login(self, email, password):
        ('id', ['username', 'email', 'password'])
        for user_id, user_data in self.database.items():
            if user_data[1] == email and user_data[-1] == password:
                print('успешно залогинились')
                return {'id':user_id, 'username':user_data[0],
                'email':user_data[1]}
        print('не правильная почта или пароль')

class GetUserMixin:
    def retrieve(self, user_id):
        user_data = self.database.get(user_id)
        return {'id': user_id, 'username':user_data[0], 'email':user_data[1]} if user_data else 'Нет такого юзера'

    def listing(self):
        return self.database

class DeleteUserMixin:
    def delete(self, user_id):
        user_data = self.database.get(user_id)
        return self.database.pop(user_id) if user_data else 'Нет такого юзера'

class UpdateUserMixin:
    def update_username(self, user_id, new_username):
        if not user_id in self.database:
            return 'пользователь не найден'
        user_data = self.database.get(user_id)
        user_data[0] = new_username
        return {'id':user_id,'username':user_data[0], 'email':user_data[1]}

    def update_password(self, user_id, new_password):
        if not user_id in self.database:
            return 'пользователь не найден'
        user_data = self.database.get(user_id)
        user_data[0] = new_password
        return {'id':user_id,'username':user_data[0], 'email':user_data[1]}


class User(
    RegisterUserMixin, 
    LoginUserMixin, 
    GetUserMixin, 
    DeleteUserMixin, 
    UpdateUserMixin
):
    database = {}

user = User()
user.register('ff_gg__yy', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user.register('name_of_user_gg', 'ff2@gmail.com', '12345678!FFd', '12345678!FFd')
ff_data = user.login('ff@gmail.com', '12345678!FFd')
user.retrieve(190)
# print(ff_data)
# print(user.database)

# написать validate_email, который будет проверять наличие сущ. email

# ToDo: CRUD - user
# listing
# retrieve
# update
# delete


# написать класс миксин GetUserMixin на получение юзеров
# retrieve - принимает в себя id юзера и возвращает след.данные: {'id':<id>, 'username':<username>, 'email':<email>}
# listing - не принимает ничего и возвращает след.данные: {'id':<id>, 'username':<username>, 'email':<email>, 'id':<id>, 'username':<username>, 'email':<email>, 'id':<id>, 'username':<username>, 'email':<email>}