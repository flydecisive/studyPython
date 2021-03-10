#step 8-10
def make_great(magicians, great_magicians):
    while magicians:
        great = 'Great ' + magicians.pop()

        great_magicians.append(great)

magicians = ['Витя', 'Толя', 'Степа']
great_magicians = []
print('Список великих фокусников: ')
def show_magicians(great_magicians):
    for magician in great_magicians:
        print('\t' + magician)

make_great(magicians, great_magicians)
show_magicians(great_magicians)

print('\nИсходный список: ')
for magician in magicians:
    print(magician)