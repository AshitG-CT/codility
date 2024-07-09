class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent)/100

    def has_slots(self):
        return hasattr(self, "__slots__")

class SlotsinspectorMixin:
    # __slots__ = ()
    def has_slots(self):
        return hasattr(self, "__slots__")
    
class Developer(SlotsinspectorMixin, Employee):
    __slots__ = ("framework", )
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

class Tester(Employee):
    def run_tests(self):
        print(f"Tester name is {self.name}, age {self.age} and his salary is {self.salary}")

employee1 = Tester('Sanket', 38, 20000)
employee2 = Developer('Amit', 40, 20000, "Flask")

employee1.increase_salary(20)
print('Salary ***** ', employee1.salary)
employee2.increase_salary(20,30)
print('name ***** ', employee2.name)
print(employee2.has_slots())
print(Developer.__mro__)
print(employee2.__dict__)