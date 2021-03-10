#step 8-9
def show_magicians(magicians):
    print('Список фокусников: ')
    for magician in magicians:
        print('\t' + magician.title())

magicians = ['Толя', 'Коля', 'Петя', 'вова']
show_magicians(magicians)