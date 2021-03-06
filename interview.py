#step 6-6
languages = {
    'Maksim': 'python',
    'Tanya': 'C',
    'Katya': 'C++',
    'Marina': 'python',
    'Roman': 'ruby',
}

participants = ['Maksim', 'Marina', 'Nikolai', 'Tanya', 'Victor']

for key in languages.keys():
    if key in participants:
        print(key + ', спасибо за участие в опросе')
    else:
        print(key + ', примите, пожалуйста, участие в опросе')