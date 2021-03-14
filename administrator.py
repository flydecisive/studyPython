#step 9-7

class User():

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print('Имя пользователя: ' + self.first_name)
        print('Фамилия пользователя: ' + self.last_name)
        print('Возраст пользователя: ' + self.age)
        print('Где находится пользователль: ' + self.location)

    def greet_user(self):
        print('Привет, ' + self.first_name + ' ' + self.last_name + '!')

class Admin(User):

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privilegies = [
            'разрешено добавлять сообщения',
            'разрешено удалять пользователей',
            'разрешено банить пользователей',
        ]

    def show_privilegies(self):
        for privilegie in self.privilegies:
            print(privilegie)

administrator = Admin('Максим', 'Мухин', '24', 'Волгоград')
administrator.show_privilegies()