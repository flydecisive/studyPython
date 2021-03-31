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

old_err_mes = 'Не возможно изменить характеристику на новое значение, '
old_err_mes += 'так как у вас не осталось свободных очков'

points = 30
characters = {}
choiced = []
health = 0
strong = 0
dexterity = 0
wisdom = 0
choice = ''

def checking_value(value, points):
    '''Функция проверяет значение для очков'''
    while value > points:
        print(err_mes)
        print('Текущее количество очков: ', points)
        value = int(input('Какое количество очков вы хотите добавить? '))
    return value

def checking_old_value(value, points, old_point):
    #if value > old_point and value - old_point > points:
    while value - old_point > points:
        print(old_err_mes)
        print('Текущее количество очков: ', points)
        value = int(input('На какое значение хотите изменить характеристику? '))
    return value

print(greeting)
print('--------------------------------------------')
while choice != '0':
    print('Текущее количество очков: ', points)
    choice = input(choice_mes)
    if choice not in choiced:
        choiced.append(choice)
        if choice == '0':
            break
        elif choice == '1':
            strong = int(input('Какое количество очков вы хотите добавить в силу? '))
            if strong > points:
                strong = checking_value(strong, points)
            characters['Сила'] = strong
            points -= strong
        elif choice == '2':
            health = int(input('Какое количество очков вы хотите добавить в здоровье? '))
            if health > points:
                health = checking_value(health, points)
            characters['Здоровье'] = health
            points -= health
        elif choice == '3':
            wisdom = int(input('Какое количество очков хотите добавить в мудрость? '))
            if wisdom > points:
                wisdom = checking_value(wisdom, points)
            characters['Мудрость'] = wisdom
            points -= wisdom
        elif choice == '4':
            dexterity = int(input('Какое количество очков хотите добавить в ловкость? '))
            if dexterity > points:
                dexterity = checking_value(dexterity, points)
            characters['Ловкость'] = dexterity
            points -= dexterity

    else:
        print('Вы назначали значение для этой характеристики.')
        answer = input('Хотите переназначить значение? (да/нет) ')
        if answer.lower() == 'да':
            if choice == '1':
                old_point = characters['Сила']
                strong = int(input('На какое значение хотите изменить характеристику? '))
                if strong > old_point and strong - old_point <= points:
                    new_point = checking_old_value(strong, points, old_point)
                else:
                    new_point = strong
                if new_point > old_point:
                    points -= (new_point - old_point)
                else:
                    points += (old_point - new_point)
                characters['Сила'] = new_point
    


print('\nВы создали персонажа со следующими характеристиками:')
for name, value in characters.items():
    print(name + ': ' + str(value))
print('Не использованные очки:', points)
