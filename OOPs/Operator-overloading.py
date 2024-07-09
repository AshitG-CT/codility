'''Operator overloading in Python refers to the ability to define a special behavior for a built-in operator (+, -, *, /, etc.) when applied to objects of a custom class. It allows objects to be manipulated using operators, and enables flexibility and natural expression of code.'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Point objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Use the + operator to add two Point objects
p3 = p1 + p2

# Display the result
print(p3)  # Output: (6, 8)
