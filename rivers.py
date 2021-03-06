#step 6-4
rivers = {
    'Volga': 'Russia',
    'Nile': 'Egypt',
    'Themse': 'Britain',
    'Nigger': 'Africa'
}

for key, value in rivers.items():
    print('The ' + key + ' runs through ' + value)

print('\n')

for key in rivers.keys():
    print(key)

print('\n')
for value in rivers.values():
    print(value)