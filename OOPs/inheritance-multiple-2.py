'''Multiple Inheritance: Multiple inheritance involves a class that inherits from two or more parent classes. The child class inherits all the attributes and methods from each parent class. Here's an example:'''
class Father:
    def __init__(self):
        self.father_property = "I am the father."
    
    def father_method(self):
        print("This is a method from the Father class.")
        

class Mother:
    def __init__(self):
        self.mother_property = "I am the mother."
    
    def mother_method(self):
        print("This is a method from the Mother class.")


class Child(Father, Mother):
    def __init__(self):
        super().__init__()


# Creating an instance of the Child class
child = Child()

print(child.father_property)  # Output: I am the father.
print(child.mother_property)  # Output: I am the mother. //AttributeError: 'Child' object has no attribute 'mother_property'. Did you mean: 'father_property'?
child.father_method()         # Output: This is a method from the Father class.
child.mother_method()         # Output: This is a method from the Mother class.
