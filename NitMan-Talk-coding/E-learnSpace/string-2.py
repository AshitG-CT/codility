'''Write a Program to reverse a string
INPUT: HELLO
OUTPUT: OLLEH'''
s = input("Enter your string: ")
print("The reverse of a string is ", s[::-1], "using list s[::-1]")
r = reversed(s)
output = ''.join(r)
print("The reverse of a string is ",output, "using join")
# Using while loop
oput = ''
i = len(s)-1
while i>=0:
    print('s[i]',i,s[i])
    oput = oput+s[i]
    i-=1
print(oput)