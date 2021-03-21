#step 9-5

class User():

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print('Имя пользователя: ' + self.first_name)
        print('Фамилия пользователя: ' + self.last_name)
        print('Возраст пользователя: ' + self.age)
        print('Где находится пользователль: ' + self.location)

    def greet_user(self):
        print('Привет, ' + self.first_name + ' ' + self.last_name + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Максим', 'Мухин', '24', 'Волгоград')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)