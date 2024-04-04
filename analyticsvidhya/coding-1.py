# https://www.analyticsvidhya.com/blog/2022/07/python-coding-interview-questions-for-freshers/

# Q1. Convert a given string to int using a single line of code.
a = '5'
print(int(a))
# Output: 5

# Q2. Write a code snippet to convert a string to a list.
str1 = "Analytics Vidhya"
print(str1.split(" "))
# Output: ['Analytics', 'Vidhya']

# Q3. Write a code snippet to reverse a string without using any in-built function.
str1 = "Analytics Vidhya"
str2 = ''

for i in str1:
    str2 = i + str2
print("The original string is: ", str1)
print("The reversed string is: ", str2)

# Q4. Write a code snippet to sort a list in Python.
my_list = [3, 2, 1]
my_list.sort()
print(my_list)
# output: [1, 2, 3]

'''
Q5. What is the difference between mutable and immutable?
Ans. Mutable objects: They can be updated once defined. e.g., list.
Immutable objects: They cannot be updated. e.g., tuples.

Q6. How can you delete a file in Python?
Ans. We can delete the file in Python using the os module. The remove() function of the os module is used to delete a file in Python by passing the filename as a parameter. e.g.

import os
os.remove("txt1.txt")
Q8. Discuss different ways of deleting an element from a list.
Ans. There are two ways in which we can delete elements from the list:

1. By using the remove() function

The remove () function deletes the mentioned element from the list.
'''
list1 = [1, 2, 3, 4]
list1.remove(2)
print(list1)
# Output: [1, 3, 4]
'''
2. By using the pop() function
Pop() function delete element mentioned at a specific index from the list
'''
list1.pop(1)
print(list1)
# Output: [1, 4]

# Q9. Write a code snippet to delete an entire list.
list3 = [1, 2, 3, 4]
list3.clear()

# Q10. Write a code snippet to reverse an array.
# 1. Using the flip() function
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.flip(arr1)
print(arr2)
# Output: [4 3 2 1]

# 2. Without using any function
arr3 = np.array([5, 6, 7, 8])
arr4 = arr3[::-1]
print(arr4)
# Output: [8 7 6 5]

# Q11. Write a code snippet to get an element, delete an element, and update an element in an array.
arr4 = [1, 2, 3, 4]
x = np.delete(arr4, 0)
print(x)
# Output: [2 3 4]

# Q12. Write a code snippet to concatenate lists: [‘We’, ‘a ‘, ‘writing’, ‘blog’]
List5= ["W", "a", "w","b"]
List6 = ["e", " ","riting","log"]
lst3 = [x+y for x, y in zip(List5, List6)]
print(lst3)
# Output: ['We', 'a ', 'writing', 'blog']

# Q13. Write a code snippet to generate the square of every element of a list.
lst4 = [1, 2, 3, 4]
lst_final = []
for x in lst4:
    lst_final.append(x * x)
print(lst_final)
# [1, 4, 9, 16]