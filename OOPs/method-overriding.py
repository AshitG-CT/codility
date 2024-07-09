'''Method overriding is when a subclass provides a different implementation of a method that is already provided in its parent class. It allows the subclass to provide its specific implementation while extending the functionality of the parent class.'''
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Cat(Animal):
    def make_sound(self):
        print("The cat says meow.")

# Creating objects
animal = Animal()
animal.make_sound()   # Output: The animal makes a sound.

cat = Cat()
cat.make_sound()      # Output: The cat says meow.
