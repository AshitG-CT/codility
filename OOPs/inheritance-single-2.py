'''Single-level Inheritance: Single-level inheritance involves a parent class and a child class. The child class inherits all the attributes and methods of the parent class. Here's an example:'''
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

class Child(Parent):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age

    def say_age(self):
        print(f"I am {self.age} year old.")
    
child = Child('priti', 23)
child.say_hello()
child.say_age()