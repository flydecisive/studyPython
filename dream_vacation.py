#step 7-10
vacations = {}
active = True

while active:
    name = input('Введите ваше имя: ')
    vacation = input('Куда бы вы хотели поехать в отпуск? ')

    vacations[name] = vacation

    question = input('Хотите дать ответить следующему пользователю? (да / нет) ')
    if question.lower() == 'нет':
        break

print('\nСписок отпусков:')
for name, vacation in vacations.items():
    print(name + ' хочет поехать в отпуск в ' + vacation)