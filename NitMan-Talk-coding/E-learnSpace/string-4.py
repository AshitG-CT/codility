'''Program to Reverse internal content of each word
Input: Welcome to Python Class
Output: emocleW ot nohtyP ssalC'''

s = input("Enter your string: ")
l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
output = ' '.join(l1)
print(output)