'''Dunder Methods
Special "magic" methods that start and end with the double underscore. Usually invoked by a special syntax.'''

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        # self.set_salary(salary)

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

    @property
    def salary(self):
        return self._salary

    # def set_salary(self, salary):
    ## setting property method
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary


e1 = Employee("ji-soo", 38, "developer", 30000)
e2 = Employee("Lauren", 44, "devops", 40000)

# e1.set_salary(2000)
e1.salary = 2000
print(e1.salary)    ## 2000