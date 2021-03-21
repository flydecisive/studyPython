#step 7-8
sandwich_orders = ['Первый', 'pastrami', 'Второй', 'pastrami', 'третий', 'pastrami']
copy_sandwich_orders = sandwich_orders[:]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print('Я сделал тебе ' + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\nВсе изготовленные сэндвичи:')
for sandwich in finished_sandwiches:
    print('\t' + sandwich)

#step 7-9
print('\n\nПастрами больше нет')
while 'pastrami' in copy_sandwich_orders:
    copy_sandwich_orders.remove('pastrami')

print('Текущий список сэндвичей:')
for sandwich in copy_sandwich_orders:
    print(sandwich)