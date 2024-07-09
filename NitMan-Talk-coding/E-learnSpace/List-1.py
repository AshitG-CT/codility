# to find max and min num from the list
list1 = [90,23,22,900,2887,21,33,244]
max=min=list1[0]
for a in list1:
    if a > max:
        max = a
print("The max num is: ", max)
for x in list1:
    if x < min:
        min = a
print("The min mun is: ", min)