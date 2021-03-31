'''Программа распределяет очки между характеристиками персонажа
по выбору пользователя'''
greeting = 'Добро пожаловать в игру!\n'
greeting += 'Предлагаем вам создать нового персонажа.\n'
greeting += 'У вас есть 30 очков и 4 характеристики: '
greeting += 'сила, здоровье, мудрость, ловкость.'

choice_mes = '''Делайте ваш выбор: 
                0 - выход
                1 - сила
                2 - здоровье
                3 - мудрость
                4 - ловкость\n
                '''

err_mes = 'Не возможно добавить столько очков, т.к. они превышают '
err_mes += 'общее количество очков. \nВведите другое значение'

points = 30
characters = {}
health = 0
strong = 0
dexterity = 0
wisdom = 0

print(greeting)
print('--------------------------------------------')
while points >= 0:
    print('Текущее количество очков: ', points)
    choice = input(choice_mes)
    if choice == '0':
        break
    elif choice == '1':
        strong = int(input('Какое количество очков вы хотите добавить в силу? '))
        if strong > points:
            while strong > points:
                print(err_mes)
                print('Текущее количество очков: ', points)
                strong = int(input('Какое количество очков вы хотите добавить в силу? '))
        characters['Сила'] = strong
        points -= strong
    elif choice == '2':
        health = int(input('Какое количество очков вы хотите добавить в здоровье? '))
        if health > points:
            while health > poitns:
                print(err_mes)
                print('Текущее количество очков: ', points)
                health = int(input('Какое количество очков вы хотите добавить в здоровье? '))
        characters['Здоровье'] = health
        points -= health
    elif choice == '3':
        wisdom = int(input('Какое количество очков хотите добавить в мудрость? '))
        if wisdom > points:
            while wisdom > points:
                print(err_mes)
                print('Текущее количество очков: ', points)
                wisdom = int(input('Какое количество очков хотите добавить в мудрость? '))
        characters['Мудрость'] = wisdom
        points -= wisdom
    elif choice == '4':
        dexterity = int(input('Какое количество очков хотите добавить в ловкость? '))
        if dexterity > points:
            while dexterity > points:
                print(err_mes)
                print('Текущее количество очков: ', points) 
                dexterity = int(input('Какое количество очков хотите добавить в ловкость? '))
        characters['Ловкость'] = dexterity
        points -= dexterity


print('\nВы создали персонажа со следующими характеристиками:')
for name, value in characters.items():
    print(name + ': ' + str(value))
print('Не использованные очки:', points)
