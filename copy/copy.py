'''https://www.simplilearn.com/tutorials/python-tutorial/python-interview-questions
83. How do you copy an object in Python?
The assignment statement (= operator) in Python does not copy objects. Instead, it establishes a connection between the existing object and the name of the target variable. The copy module is used to make copies of an object in Python. Furthermore, the copy module provides two options for producing copies of a given object –
Deep Copy: Deep Copy recursively replicates all values from source to destination object, including the objects referenced by the source object.
'''
from copy import copy, deepcopy

list_1 = [1, 2, [3, 5], 4]

## shallow copy

list_2 = copy(list_1) 

list_2[3] = 7

list_2[2].append(6)

list_2    # output => [1, 2, [3, 5, 6], 7]

list_1    # output => [1, 2, [3, 5, 6], 4]

## deep copy

list_3 = deepcopy(list_1)

list_3[3] = 8

list_3[2].append(7)

list_3    # output => [1, 2, [3, 5, 6, 7], 8]

list_1    # output => [1, 2, [3, 5, 6], 4]
'''
Shallow Copy: A bit-wise copy of an object is called a shallow copy. The values in the copied object are identical to those in the original object. If one of the values is a reference to another object, only its reference addresses are copied.
'''