'''Program to find index of particular character of string'''
s = input("Enter your string: ")
subs = input("Enter your sub string: ")

flag = False
pos = -1
n = len(s)
count = 0
while True:
    pos = s.find(subs, pos+1, n)
    if pos == -1:
        break
    print("Found at index: ",pos)
    flag = True
    count =+1
if flag == False:
    print("Not Found.")
print("The no. of occurrances: ", count)

'''Output:
Enter your string: Python is very easy easy to learn
Enter your sub string: asy
Found at index:  15
Found at index:  20

The no. of occurrances: 1
'''