def first_word(text):
    '''Функция вовзращает первое слово в строке'''
    count = 0
    i = 0
    peace = ''
    #for letter in text:

    while True:
        if not text[i].isalpha():
            count += 1
            peace = text[count:]
        elif text[i].isalpha():
            a = count
            if len(peace) == 0:
                peace = text[:]
            for pe in peace:
                if pe == '.' or pe == ' ' or pe == ',':
                    ind = peace.index(pe)
                    answer = peace[:ind]
                    break
                a += 1
                if a > 0:
                    answer = peace
            break
        i += 1
    
    return answer

print(first_word("Hello.World"))
