# Create a program by following these requirements:
# 1. Create a class called "Human"
# 2. Initialize the class with "name" and "age" attributes which are both private
# 3. Create a method called "talk" that prints "Hello, my name is {name} and I am {age} years old
# Nice to meet you!"
# 4. Create a method __str__ that returns the name and age of the human
# 5. Create a class called "Police" that inherits from "Human"
# 6. Create a method called "arrest" that prints "เอาเงินมาจะปล้น 0.0"
# 7. Create a method called "pewww" that prints "ฉีดยาเพื่อปล่อยตัว"

class Human:
    pass


class Police(Human):
    pass


if __name__ == '__main__':
    human = Human("Bob", 20)
    human.talk()
    print(human)
    police = Police("Police", 30)
    print(police)
    police.talk()
    police.arrest()
    police.pewww()
