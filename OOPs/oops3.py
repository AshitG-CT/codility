'''Telusko: OOP in Python | Object Oriented Programming
Inner class:
You can create object of inner class inside the outer class
OR
You can create object of inner class outside the outer class provided you use outer class name to call it'''

class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print('Brand: '+self.brand, 'CPU: '+self.cpu, 'RAM: '+str(self.ram))

s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)

s1.show()

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))

s1.lap.brand = 'Dell'
s1.lap.cpu = 'i7'
s1.lap.ram = 16
print(s1.lap.brand, s1.lap.cpu, s1.lap.ram)
lap1 = Student.Laptop().show()
lap2 = Student.Laptop().show()
print(lap1)
print(lap2)

'''Output
Navin 2
Brand: HP CPU: i5 RAM: 8'''