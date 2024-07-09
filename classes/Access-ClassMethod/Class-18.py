## Data type hinting
from dataclasses import dataclass

## We can replace this with data classes
# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client

#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"

@dataclass
class Project:
    name: str
    payment: str
    client: str

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project
        
p = Project("Django app", 20000, "Globalmantic")
e = Employee("Ji-Soo", 38, 10000, p)

print(e.project)