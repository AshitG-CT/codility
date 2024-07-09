n = int(input("Enter no. of students: "))
d = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter students marks: "))
    d[name] = marks
print(d)
while True:
    name = input("Enter student name to know marks: ")
    marks = d.get(name, -1)
    if marks == -1:
        print("Student not found")
    else:
        print("The marks of {}: {} ".format(name, marks))
    option = input("Do you wnat to find another student marks [Yes/ No]")
    if option == "No":
        break
    print("Thanks for using our application")