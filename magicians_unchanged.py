#step 8-11
def make_great(magicians, great_magicians):
    while magicians:
        current_magician = 'Great ' + magicians.pop()

        great_magicians.append(current_magician)

def show_magicians(great_magicians):
    print('\nСписок фокусников: ')
    for magician in great_magicians:
        print('\t' + magician)

magicians = ['Вова', 'Толя', 'Рома']
great_magicians = []

make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
print('\nИсходный список: ')
for magician in magicians:
    print(magician)