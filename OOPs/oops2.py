'''Telusko: OOP in Python | Object Oriented Programming
Link: https://www.youtube.com/watch?v=qiSCMNBIP2g
https://www.youtube.com/watch?v=qiSCMNBIP2g'''

# class Car:
#     wheels = 4 # class variable

#     def __init__(self) -> None:
#         self.mil = 10 # instance variable
#         self.com = "BMW"
        
# c1 = Car()
# c2 = Car()

# c1.mil = 8
# c2.wheels = 5

# print(c1.com, c1.mil, c1.wheels)
# print(c2.com, c2.mil, c2.wheels)

'''Output
BMW 8 4
BMW 10 5'''


'''Class method cls, static method'''
class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
        
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is Student class.. in this module")

s1 = Student(34, 47, 32)
s2 = Student(89,32, 12)

print(s1.avg())
print(Student.getSchool())

Student.info()

'''OutPut
37.666666666666664
Telusko
This is Student class.. in this module'''