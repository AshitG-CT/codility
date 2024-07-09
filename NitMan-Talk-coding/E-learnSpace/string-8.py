'''Program to sort characters of the string first alphabet and then Strings
Input: B4A1D3
Output: ABD134'''
s = input("enter your alphanumber string: ")

s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 = s1+x
    elif x.isdigit():
        s2 = s2 + x

for x in sorted(s1):
    output = output+x
for x in sorted(s2):
    output = output+x

print(output)