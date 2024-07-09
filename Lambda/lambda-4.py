'''Reducing:
The reduce() Function  works differently than map() and filter(). It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.
Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

The syntax is:
reduce(function, sequence[, initial])
'''
# Calculate the sum of all elements in a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print('Calculate result: ', result)  # Output: 15

# Find the maximum number in a list
numbers = [10, 5, 20, 15, 8]
result = reduce(lambda x, y: x if x > y else y, numbers)
print('Maximum result: ', result)  # Output: 20

# Find the maximum number is a list which have duplicate numbers
list_125 = [5, 1, 6, 2, 8, 3, 8, 2, 5, 9, 1, 5, 7, 9]
list_125 = set(list_125)
list_125.remove(max(list_125))
result_list_125 = reduce(lambda x, y: x if x > y else y, list_125)
print('Second Maximum: ', result_list_125)

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))