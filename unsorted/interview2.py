#step 10-5
file_name = 'interview.txt'
question = 'Почему вам нравится програмировать?\n'
question += 'Введите ответ на вопрос или "quit" чтобы выйти: '

with open(file_name, 'a') as file_object:
    while True:
        answer = input(question)
        if answer.lower() == 'quit':
            break
        file_object.write(answer + '\n')
