'''Program to reverse order of words present in the given string
Input: Learning Python is very easy
Output: easy very is Python Learning'''
s = input("Enter your string: ")
l = s.split()
print(l)
l1 = l[::-1]
output = ' '.join(l1)
print(output)