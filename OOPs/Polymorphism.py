'''Polymorphism in Python refers to the ability of an object to take on multiple forms or have multiple behaviors. In other words, objects of different classes can be treated as objects of a common base class.'''
class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
