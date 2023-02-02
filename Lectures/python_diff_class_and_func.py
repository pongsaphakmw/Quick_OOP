def create_people(name, age):
    return {'name': name, 'age': age}


def create_people_without_return(name, age):
    pass


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    people1 = create_people('John', 20)
    people2 = People('John', 20)
    print()
    print(people1)
    print(people2)
    print('people1 is dict: ', isinstance(people1, dict))
    print('people2 is dict: ', isinstance(people2, dict))
    print('attribute name of people1: ', people1['name'])
    print('attribute name of people2: ', people2.name)
    print()
    # what if we didn't return a dict in create_people?
    people3 = create_people_without_return('John', 20)
    print('attribute name of people3: ', people3['name'])
    print()
