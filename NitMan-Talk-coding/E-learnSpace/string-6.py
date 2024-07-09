'''Program to find index of particular character of string'''
s = input("Enter your string: ")
subs = input("Enter your sub string: ")

flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(subs, pos+1, n)
    if pos == -1:
        break
    print("Found at index: ",pos)
    flag = True
if flag == False:
    print("Not Found.")

'''Output:
Enter your string: Python is very easy to learn
Enter your sub string: very
Found at index:  10

Enter your string: python is easy to learn
Enter your sub string: hard
Not Found.
'''