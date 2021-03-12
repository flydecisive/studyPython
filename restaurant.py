#step 9-1
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('Имя ресторана: ' + self.restaurant_name)
        print('Тип кухни: ' + self.cuisine_type)
    
    def open_restaurant(self):
        print('Ресторан открыт')

restaurant = Restaurant('У Татьяны', 'Смешанная')
print('Имя ресторана: ' + restaurant.restaurant_name)
print('Тип кухни: ' + restaurant.cuisine_type)

print('Описание первого ресторана: ')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#step 9-2

print('Описание второго ресторана: ')
second_restaurant = Restaurant('У Вазгена', 'Грузинская')
second_restaurant.describe_restaurant()

print('Описание третьего ресторана: ')
third_restaurant = Restaurant('Кузно', 'Итальянская')
third_restaurant.describe_restaurant()