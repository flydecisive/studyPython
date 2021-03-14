#step 9-9

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_car(self):
        print('Описание автомобиля: ')
        print('\t' + self.make)
        print('\t' + self.model)
        print('\t' + self.year)

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def get_range(self):
        if self.battery.battery_size == 70:
            range = 240
        elif self.battery.battery_size == 85:
            range = 270
        
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge'
        print(message)

my_car = ElectricCar('Tesla', 'Model S', '2021')
my_car.show_car()
my_car.get_range()
my_car.battery.upgrade_battery()
my_car.get_range()
