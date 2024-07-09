class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

e1 = Employee("ji-soo", 38, "developer", 30000)
e2 = Employee("Lauren", 44, "devops", 40000)

print(e1.name)
print(e2.name)