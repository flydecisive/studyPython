#step 10-4
file_name = 'guest_book.txt'
message = 'Введите имя пользователя или '
message += '"quit" что бы выйти: '

with open(file_name, 'a') as file_object:
    while True:
        data = input(message)
        if data.lower() == 'quit':
            break
        greeting = 'Hello, ' + data
        print(greeting)
        file_object.write(greeting + '\n')