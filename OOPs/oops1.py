'''Telusko: OOP in Python | Object Oriented Programming
Link: https://www.youtube.com/watch?v=qiSCMNBIP2g
https://www.youtube.com/watch?v=qiSCMNBIP2g'''

# class Computer:
#     def config(self):
#         print("i5, 16gb, 1TB")

# com1 = Computer()
# com2 = Computer()

# Computer.config(com1)
# Computer.config(com2)

# com1.config()
# com2.config()

'''
Output:
i5, 16gb, 1TB
i5, 16gb, 1TB
i5, 16gb, 1TB
i5, 16gb, 1TB
'''

# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram

#     def config(self):
#         print("config is ", self.cpu, self.ram)

# com1 = Computer('i5', 16)
# com2 = Computer('Gen 3', 8)

# Computer.config(com1)
# Computer.config(com2)

# com1.config()
# com2.config()

'''Output:
config is  i5 16
config is  Gen 3 8
config is  i5 16
config is  Gen 3 8'''

# class Computer:
#     def __init__(self):
#         self.name = "Ashit"
#         self.age = 32

#     def update(self):
#         self.age = 34

#     def config(self):
#         print("config is ", self.name, self.age)

# com1 = Computer()
# com2 = Computer()

# com1.name = "Manish"
# com1.age = 12
# com1.update()

# com1.config()
# com2.config()

'''Output
config is  Manish 34
config is  Ashit 32
'''

class Computer:
    def __init__(self):
        self.name = "Ashit"
        self.age = 32

    def compare(self, other):
        print('other : ', other.age)
        print('self : ', self.age)
        if self.age == other.age:
            return True
        else:
            return False

    def config(self):
        print("config is ", self.name, self.age)

com1 = Computer()
com1.age = 12
com2 = Computer()

if com1.compare(com2):
    print("They are same")
else:
    print("They are different")

com1.config()
com2.config()

'''Output
They are different
config is  Ashit 12
config is  Ashit 32'''