class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Human):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # super() is used to call the parent class
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class Teacher(Human):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Subject: {self.subject}"


if __name__ == "__main__":
    human = Human("John", 30)
    print(human)

    student = Student("Jane", 20, 90)
    print(student)

    teacher = Teacher("Jack", 40, 1000, "Math")
    print(teacher)
