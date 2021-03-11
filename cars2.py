#step 8-14
def make_car(manufacturer, model, **parametrs):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in parametrs.items():
        car[key] = value
    return car

print('Параметры автомобиля: ')
print(make_car('Lada', 'Vesta', color='black', tow_package=False, price='600 000'))