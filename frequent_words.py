#step 10-10
books = ['grant.txt', 'mesa.txt']
word = 'the'

for book in books:
    try:
        with open(book) as file_object:
            reading = file_object.read()
    except FileNotFoundError:
        print('Файл ' + book + ' не найден')
    else:
        num = reading.lower().count(word)
        print('В файле ' + book + ' ' + str(num) + ' слов "the"')