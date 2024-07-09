'''Input: a4b3c2
Output: aaaabbbcc'''
s = input("Enter some string: ")
output = ''
for x in s:
    if s.isalpha():
        previous = x
    elif x.isdigit():
        output = output+previous*int(x)
print(output)