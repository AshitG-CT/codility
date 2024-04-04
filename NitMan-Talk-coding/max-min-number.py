# Find the maximum and minimum value from a list without using any predefine function:
l = [9, 11, 0, 370, 55, 0, 2]
maximum = l[0]
minimum = l[0]

for i in l:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print('Maximum: ', maximum)
print('Minimum: ', minimum)