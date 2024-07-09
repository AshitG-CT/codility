'''Inheritance is a key concept in object-oriented programming that allows classes to inherit the properties and methods of other classes. In Python, there are three types of inheritance: single level, multilevel, and multiple inheritance.

Single-level Inheritance: Single-level inheritance involves a parent class and a child class. The child class inherits all the attributes and methods of the parent class. Here's an example:'''
class A:
    def feature1(self):
        print("Feature A-1 working")

    def feature2(self):
        print("Feature A-2 working")


class B(A):
    def feature3(self):
        print("Feature B-3 working")

    def feature4(self):
        print("Feature B-4 working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
