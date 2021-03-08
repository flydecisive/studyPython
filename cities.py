#step 6-11
cities = {
    'Volgograd': {
        'Country': 'Russia', 
        'Population': 'Over 1 000 000',
        'Fact': 'Any fact',
    },
    'New York': {
        'Country': 'USA',
        'Population': 'Over 7 000 000',
        'Fact': 'Any fact',
    },
    'Moscow': {
        'Country': 'Russia',
        'Population': 'Over 15 000 000',
        'Fact': 'Some fact',
    },
}

for city, parametrs in cities.items():
    print('Параметр города ' + city + ':')
    for parametr in parametrs.values():
        print('\t' + parametr)
    print('\n')