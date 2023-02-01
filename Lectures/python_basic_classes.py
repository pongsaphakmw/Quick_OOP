class Human:
    name = 'John'
    age = 30
    country = 'USA'

class City:
    name = 'New York'
    population = 10000000
    country = 'USA'

    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country


class Flowers:
    def __init__(self, name, color, price):
        self.__name = name
        self._color = color
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def change_color(self, new_color):
        self._color = new_color
    
    def change_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name


class GroundFlowers(Flowers):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)


        

if __name__ == '__main__':
    print(Human)
    print('Human name is', Human.name)
    print('Human age is', Human.age)
    print('Human country is', Human.country)
    print()
    print(City)
    print('City name is', City.name)
    print('City population is', City.population)
    print('City country is', City.country)
    print()
    print('Creating a new city')
    new_city = City('London', 1000000, 'UK')
    print('New city name is', new_city.name)
    print('New city population is', new_city.population)
    print('New city country is', new_city.country)
    print('Printing all attributes of new city in dictionary format')
    print(new_city.__dict__)
    print()

    print('Creating a new flower')
    new_flower = Flowers('Rose', 'Red', 10)

    try:
        print('Get flower name using normal way')
        print('Flower name is', new_flower.__name)
    except AttributeError:
        print('Get flower from get_name() method')
        print('Flower name is ', new_flower.get_name())
    print('Flower color is', new_flower._color)
    print('Getting flower color using get_color() method')
    print('Flower color is', new_flower._color)
    print('Flower price is', new_flower.price)
    print()

    print('Changing new flower price to 20')
    new_flower.change_price(20)
    print('New flower price is', new_flower.price)
    print('Changing new flower color to Blue')
    new_flower.change_color('Blue')
    print('New flower color is', new_flower._color)
    print('Changing new flower name to Daisy')
    new_flower.change_name('Daisy')
    print('New flower name is', new_flower.get_name())
    print()

    print('Creating a new ground flower')
    new_ground_flower = GroundFlowers('Daisy', 'Blue', 20)
    print('New ground flower name is', new_ground_flower.get_name())
    