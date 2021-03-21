#step 9-4
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Название ресторана: ' + self.restaurant_name)
        print('Тип кухни: ' + self.cuisine_type)

    def restaurant_open(self):
        print('Ресторан ' + self.restaurant_name + 'открыт.')

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
    
restaurant = Restaurant('У Максима', 'Итальянская')
print(restaurant.number_served)
restaurant.set_number_served(2)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)