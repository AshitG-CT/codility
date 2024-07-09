##https://app.pluralsight.com/ilx/video-courses/a4c8f304-85a0-441c-8062-b31ece699072/9bd8307a-ea7e-44fa-9c81-1d7648bb3bd0/08ecf362-b697-405c-a46a-216d173463e1

## In python every thing is object
# name = 'Evernorth'
# i = 5

# print(name.__class__)
# print(i.__class__)

# class Employee:
#     pass


# e = Employee()
# print(e.__class__)  ## <class '__main__.Employee'>
# print(e.__dict__)  ## {}

# class Employee:
#     def __init__(self) -> None:
#         self.__dict__["name"] = "Ji-Suo"
#         self.__dict__["age"] = 38
#         self.__dict__["position"] = "Team lead"
#         self.__dict__["salary"] = 30000


# e = Employee()
# print(e.__dict__)   ## {'name': 'Ji-Suo', 'age': 38, 'position': 'Team lead', 'salary': 30000}
# print(e.__class__)  ## <class '__main__.Employee'>

class Employee:
    def __init__(self) -> None:
        self.name = "Ji-Suo"
        self.age = 38
        self.position = "Team lead"
        self.salary = 30000


e = Employee()
print(e.name)       ## Ji-Suo
print(e.__class__)  ## <class '__main__.Employee'>


