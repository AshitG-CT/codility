'''Program for the requirement
Input: HELLO
Inout: WORLD
Output: HWEOLRLLOD'''
s1 = input("Enter your first string: ")
s2 = input("Enter your second string: ")

output = ''
i=j=0
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output = output+s1[i]
        i+=1
    if j < len(s2):
        output = output+s2[j]
        j+=1
print(output)