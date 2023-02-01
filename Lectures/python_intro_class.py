class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    

if __name__ == '__main__':
    print(Car)
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car)
    print(my_new_car.get_descriptive_name())
    print(my_new_car.make)