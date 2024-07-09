'''Program to reverse internal content of every seconfd word present in the give string
Input: one two three four five
Output: one owt three rouf five'''
s = input("Enter your string: ")
l = s.split()
i = 0
l1 = []
while i < len(i):
    if i % 2 == 0:
        l1.append(l[i][::-1])
    else:
        l1.append(l[i][::-1])
    i+=1
output = ' '.join(l1)
print(output)