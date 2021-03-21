#step 9-6
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('Имя ресторана: ' + self.restaurant_name)
        print('Тип кухни: ' + self.cuisine_type)
    
    def open_restaurant(self):
        print('Ресторан открыт')

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Черничное', 'Шоколадное', 'Пломбир']

    def describe_flavours(self):
        for flavour in self.flavours:
            print(flavour)

ice_cream_stand = IceCreamStand('Морожко', 'Кафе-мороженое')
ice_cream_stand.describe_restaurant()
print('Наши виды мороженого: ')
ice_cream_stand.describe_flavours()