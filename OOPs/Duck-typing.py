'''Duck typing is a concept in Python and other dynamic programming languages where the object's suitability for a particular function or method is determined by the presence of certain methods and properties, rather than by the type of the object itself. It focuses on the object's behavior rather than its type.'''

class Duck:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("Flying!")

class Robot:
    def speak(self):
        print("Hello!")

    def move(self):
        print("Walking!")

def make_it_quack(obj):
    obj.quack()

duck = Duck()
robot = Robot()

make_it_quack(duck)  # Output: "Quack!"
make_it_quack(robot)  # Output: Error - 'Robot' object has no attribute 'quack'
