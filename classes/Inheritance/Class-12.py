class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        print('print percent ****** : ', percent)
        self.salary += self.salary * (percent)/100

class Developer(Employee):
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent)/100
        self.salary += bonus

class Tester(Employee):
    def run_tests(self):
        print(f"Tester name is {self.name}, age {self.age} and his salary is {self.salary}")

employee1 = Tester('Sanket', 38, 20000)
employee2 = Developer('Amit', 40, 20000)
employee1.run_tests()
employee1.increase_salary(20)
print(employee1.salary)
employee2.increase_salary(20, 30)
print(employee2.salary)