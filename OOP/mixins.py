# Миксины - классы расширители, от которых мы насдледуемся, от миксинов мы не создаем обьект

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плавать')

class Human(WalkMixin, SwimMixin):
    name = 'человек'
    def talk(self):
        print('я умею говорить')

class Bird(FlyMixin):
    pass

class Fish(SwimMixin):
    pass

class FlyFish(SwimMixin, FlyMixin):
    name = 'flyfish'
    
    def __init__(self, name) -> None:
        self.name = name



# a = [1,2,3,4]
# print(isinstance(a, str))
# print(isinstance(FlyFish, FlyMixin))
# print(issubclass(list, tuple))
# flyfish = FlyFish('xdcfvg')
# print(flyfish.name)
# a = [1,2,3,4,5]
# print(hasattr(flyfish, 'fly'))
# print(hasattr(a, 'insert'))

# print(getattr(flyfish, 'nae', 'не найдено'))

# setattr(flyfish, 'nam', 5)

# CRUD
# create
# read
# update
# delete

# import datetime

# #lets get the current date and time
# now = datetime.datetime.now()
# print('Using str: ' + now.__str__())
# print('Using repr: ' + now.__repr__())

class BornMixin:
    def born(self, name, date):
        self.db_human.update({name.lower(): date})

class ShowMixin:
    def show(self, name):
        name = name.lower()
        if name not in self.db_human:
            return 'такого человека не существует'
        for key, value in self.db_human.items():
            if key == name:
                return f'вот вам {key.title()}, который родился в {value}'

class UpdateMixin:
    def update_name(self, name, new_name):
        name = name.lower()
        new_name = new_name.lower()
        if name not in self.db_human:
            return 'такого человека не существует'
        value = self.db_human.pop(name)
        self.db_human[new_name] = value

class KillMixin:
    def kill(self, name, method_of_murder):
        name = name.lower()
        if name not in self.db_human:
            return 'не нашел'
        self.db_human.pop(name)
        return f'успешно был убит {name} при обстаятельстве {method_of_murder}'

class CRUD(
    BornMixin, 
    ShowMixin, 
    UpdateMixin, 
    KillMixin
):
    ...

class Human(CRUD):
    db_human = {}
    # def __init__(self) -> None:

    def __str__(self) -> str:
        return f'{self.db_human}'

human = Human()
human.born('Nikita', '27-11')
print(human.show('NIKITA'))
human.update_name('Nikita', 'Tima')
print(human.show('tima'))
print(human.kill('tima', 'сбила машина и переродился в другом мире'))
