'''Dunder Methods
Special "magic" methods that start and end with the double underscore. Usually invoked by a special syntax.'''
from datetime import date

class Employee:
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is Bankrupt")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

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
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary


# e1 = Employee("ji-soo", 38, "developer", 30000)
# e2 = Employee("Lauren", 44, "devops", 40000)

e = Employee.new_employee("Mary", date(1986, 9, 18))
print(e.name)
print(e.age)
print(e.salary)