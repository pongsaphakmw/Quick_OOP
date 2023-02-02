class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("My name is {} and i'm {} years old".format(self.name, self.age))

    def eat(self):
        print("I am eating")


class Dog(Animals):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("My name is {} and I am a {}".format(self.name, self.breed))

    def bark(self):
        print("I am barking")


if __name__ == '__main__':
    print()
    animal = Animals("Bob", 5)
    animal.speak()
    animal.eat()
    print()
    dog = Dog("Dog", 3, "Labrador")
    dog.speak()
    dog.eat()
    dog.bark()
    print()
