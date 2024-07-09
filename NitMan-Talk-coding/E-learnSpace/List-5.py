''' print the nums of a specified list after removing even nums from it'''
num = [23,45,223,56,2,4,56,67]
num = [x for x in num if x%2!=0]
print(num)