#step 7-5
while True:
    message = 'Введите возраст чтобы узнать цену\n'
    message += 'Или "quit" чтобы выйти.'
    print(message)
    age = input('Введите ваш возраст: ')
    if age == 'quit':
        break
    elif int(age) < 3:
        answer = '\tДля вас билет бесплатен'
    elif int(age) >= 3 and int(age) <= 12:
        answer = '\tДля вас билет стоит 10$'
    elif int(age) > 12:
        answer = '\tДля вас билет стоит 15$'
    
    
    print(answer + '\n')