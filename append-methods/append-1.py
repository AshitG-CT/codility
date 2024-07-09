'''The append, extend, and insert are all methods used to add elements to a list in Python, but they behave differently:

append(): Syntax: list.append(element)
The append() method is used to add a single element at the end of a list.
It adds a single element to the end of the list.
The element is passed as an argument to the method.
Example: my_list.append(5) would add the element 5 at the end of the my_list list.'''
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

'''extend():
Syntax: list.extend(iterable)
The extend() method is used to add multiple elements to the end of a list. The input can be any iterable (e.g., list, tuple, string)
It adds multiple elements to the end of the list.
The elements are passed as an iterable (another list or a tuple) to the method.
The iterable is unpacked, and its elements are added individually to the list.
Example: my_list.extend([1, 2, 3]) would add the elements 1, 2, and 3 at the end of the my_list list.
'''
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


'''insert():
Syntax: list.insert(index, element)
The insert() method is used to insert an element at a specific index in the list. All elements after the inserted element will be shifted to the right.
It adds a single element at a specific index in the list.
It takes two arguments, the index where the element should be inserted, and the element itself.
All elements from the given index to the end of the list will be shifted one position to the right.
Example: my_list.insert(2, 'apple') would insert the element 'apple' at index 2 in the my_list list, and push the existing element at index 2 one position to the right.
'''
my_list = [1, 2, 3]
my_list.insert(3, 5)
print(my_list)  # Output: [1, 2, 3, 5]

my_list1 = [1,2,3]
my_list1.insert(2, "apple")
print(my_list1)
