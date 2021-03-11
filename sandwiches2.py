#step 8-12
def sandwiches(*filling):
    print('Наполнение сэндвича: ')
    for fill in filling:
        print('\t- ' + fill)

sandwiches('Лук', 'Колбаса', 'Сыр')
print()
sandwiches('Арахисовая паста')
print()
sandwiches('Соус', 'Ветчина', 'Сыр', 'Салат')