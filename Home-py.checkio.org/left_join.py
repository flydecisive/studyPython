def left_join(phrases):
    '''Функция объединяет строки и меняет право на лево'''
    text = []
    some_text = []
    for phrase in phrases:
        if 'right' in phrase:
            words = phrase.split(' ')
            for word in words:
                start_position = word.index('right')
                new_word = word[0:start_position] + 'left'
                new_word += word[len(new_word) + 1: len(word) + 1]
                some_text.append(new_word)
            text.append(' '.join(some_text))
            some_text = []
        else:
            text.append(phrase)

    answer = ', '.join(text)
    return answer

print(left_join(('bright', 'aright', 'bright', 'ok')))