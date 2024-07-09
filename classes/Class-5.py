'''Dunder Methods
Special "magic" methods that start and end with the double underscore. Usually invoked by a special syntax.'''

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} year old. Employee is a {self.position} with the salary of Rs.{self.salary}"

    def __repr__(self):
        return (
                f"Employee("
                f"{repr(self.name)}, {repr(self.age)}, "
                f"{repr(self.position)}, {repr(self.salary)})"
        )


e1 = Employee("ji-soo", 38, "developer", 30000)
e2 = Employee("Lauren", 44, "devops", 40000)

print(repr(e1))     ## Employee(ji-soo, 38, developer, 30000)

print(eval(repr(e1)))   ## NameError: name 'ji' is not defined
## ji-soo is 38 year old. Employee is a developer with the salary of Rs.30000
