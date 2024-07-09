# https://www.youtube.com/watch?v=wC69iMuYz9Q&list=PLAATA1LoNW0HYJR-26lXZqgfgrnCiEiHC
'''Write a programm to remove duplicate characters from the given input string.
Input: MISSISSIPPI
Output: MISP '''

s = input("Enter your string: ")
output = ''
for ch in s:
    if ch not in output:
        output = output+ch
print(output)

# Using list
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
output = ''.join(l)
print(output)
