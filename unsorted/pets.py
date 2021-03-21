#step 6-8
pryanik = {
    'type': 'cat', 
    'owner': 'Maksim and Tanya',
}

rada = {
    'type': 'dog',
    'owner': 'Dima',
}

pets = [pryanik, rada]

for pet in pets:
    for key, value in pet.items():
        print(key + ': ' + value)
    print('\n')