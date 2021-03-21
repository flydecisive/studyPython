def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    count = 0
    letter = ''
    while letter != ' ':
        letter = text[count]
        count += 1
        if count == len(text) and letter != ' ':
            count = len(text)
            break

    return text[0:count].rstrip()

print(first_word('hi'))
