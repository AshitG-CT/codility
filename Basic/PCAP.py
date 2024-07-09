print(9 % 6 % 2)
# from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
print(2 ** 2 ** 3)
# the exponentiation operator uses right-sided binding. 2 ** 3 → 8; 2 ** 8 → 256
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
print(eval(4 % -2))
print(12 % 4) # 0
print(12 % 4.5) # 3.0
print(12 // 4) # 3
print(12 // 4.5) # 2.0
print(2.0 * 4.5) # 9.0
print(12 - 9.0) # 3.0

'''Keyword: They are called keywords or (more precisely) reserved keywords. They are reserved because you mustn't use them as names: neither for your variables, nor functions, nor any other named entities you want to create.
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']'''
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c) # c = 5.0

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x =  -1
x = float(x)
# write your code here
y = 3*x*x*x - 2 * x **2 + 3*x - 1
print("y =", y)


print("+" + "-" * 10 + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + "-" * 10 + "+")


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


end_hour = (mins + dura) // 60
print("end_hour 1: ", end_hour)
end_hour = (hour + end_hour)
print("end_hour 2: ", end_hour)
end_hour = end_hour % 24
print("end_hour 3: ", end_hour)

end_min = (mins + dura)
print("end_min ", end_min)
end_min %= 60
print(f"{end_hour}:{end_min}")
