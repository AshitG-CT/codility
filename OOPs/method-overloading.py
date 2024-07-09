'''Method overloading is when multiple methods with the same name but different parameters are declared in a class. Python does not support method overloading natively, as it dynamically resolves the method calls at runtime. However, method overloading can be achieved by using default arguments or using a single method with conditional statements.'''
class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

# Creating an object
calc = Calculator()
print(calc.add(1, 2))          # Output: Error - add() missing 1 positional argument
print(calc.add(1, 2, 3))       # Output: 6
