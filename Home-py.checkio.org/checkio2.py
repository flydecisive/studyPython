def checkio(words):
    '''Функция считает есть ли в переданной строке три слова подряд'''
    count = 0
    answer = False
    word_list = words.split(' ')
    for word in word_list:
        if word.isalpha():
            count += 1
            if count == 3:
                answer = True
                break
        else:
            count = 0
    
    return answer
    
print(checkio('star 5 one two three 7'))