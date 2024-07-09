# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary

#     def increase_salary(employee, percent):
#         employee.salary += employee.salary * (percent/100)

#     def info(employee):
#         print(f"{employee.name} is {employee.age} year old. Employee is a {employee.position} with the salary of Rs.{employee.salary}")


# e1 = Employee("ji-soo", 38, "developer", 30000)
# e2 = Employee("Lauren", 44, "devops", 40000)

# Employee.increase_salary(e2, 20)
# Employee.info(e2)

## with self keyword
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def info(self):
        print(f"{self.name} is {self.age} year old. Employee is a {self.position} with the salary of Rs.{self.salary}")


e1 = Employee("ji-soo", 38, "developer", 30000)
e2 = Employee("Lauren", 44, "devops", 40000)

e2.increase_salary(20)
e2.info()

## Lauren is 44 year old. Employee is a devops with the salary of Rs.48000.0