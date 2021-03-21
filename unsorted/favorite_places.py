#step 6-9
favorite_places = {
    'Максим': ['Волгоград', 'Смоленск'],
    'Таня': ['Казань', 'Краснодар', 'Питер'],
    'Бабушка': ['Дача'],
}

for key, value in favorite_places.items():
    print(key + ':')
    for place in value:
        print('\t' + place)
    print('\n')