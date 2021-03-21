#step 6-7
human_1 = {
    'first_name': 'Максим',
    'second_name': 'Мухин',
    'age': 24,
    'city': 'Volgograd',
}

human_2 = {
    'first_name': 'Таня',
    'second_name': 'Столец',
    'age': 23,
    'city': 'Volgograd',
}

human_3 = {
    'first_name': 'Катя',
    'second_name': 'Мухина',
    'age': 23,
    'city': 'Volgograd'
}

humans = [human_1, human_2, human_3]

for human in humans:
    for value in human.values():
        print(value)
    print('\n')