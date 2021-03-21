#step 10-8
filename = ['cats.txt', 'dogs.txt']
for file in filename:
    try:
        with open(file) as file_object:
            print(file_object.read())
    except FileNotFoundError:
        print('Файл ' + file + ' не найден')


#step 10-9
print('\nNext step\n')
filename = ['cats.txt', 'dogs.txt']
for file in filename:
    try:
        with open(file) as file_object:
            print(file_object.read())
    except FileNotFoundError:
        pass