#step 10-3
name = input('Введите ваше имя: ')
file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    file_object.write('User name is ' + name)