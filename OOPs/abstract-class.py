'''an abstract class is a class that cannot be instantiated and acts as a blueprint for other classes to be derived from. It typically contains abstract methods that must be implemented by the derived classes. Abstract classes define the common structure and behavior that the derived classes should have.

An abstract method is a method declared in an abstract class but does not have an implementation. It is meant to be overridden by the derived classes, providing the specific implementation for that method.

Here's an example to demonstrate abstract classes and abstract methods in Python using the abc module:'''
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Creating objects of derived classes
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Accessing the overridden methods
print(rectangle.area())  # Output: 50
print(rectangle.perimeter())  # Output: 30
print(circle.area())  # Output: 153.93849
print(circle.perimeter())  # Output: 43.98226
