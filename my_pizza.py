#step 4-11
my_pizzas = ['Сырная', 'Пеперони', 'Деревенская', 'Барбекю', 'Гавайская']
friend_pizzas = my_pizzas[:]
my_pizzas.append('Чепотл')
friend_pizzas.append('Фермерская')

print('My favorite piizas are:')
for pizza in my_pizzas:
    print(pizza)

print('My friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)