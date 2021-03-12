#step 9-3

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

new_user = User('Максим', 'Мухин', '24', 'Волгоград')
print('Встречайте нового пользователя: ')
new_user.describe_user()
