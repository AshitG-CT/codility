'''Multilevel Inheritance: Multilevel inheritance involves multiple levels of inheritance chain. The child class inherits from a derived class, which further inherits from its parent class. Here's an example:'''
class GrandParent:
    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print(f"Hello, My name is {self.name}.")

class Parent(GrandParent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_age(self):
        print(f"My age is {self.age}.")

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def say_school(self):
        print(f'My schoole is {self.school}')

child = Child('priti', 23, 'Vivekanand school.')
child.say_hello()
child.say_age()
child.say_school()