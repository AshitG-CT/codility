'''Sorting a list of tuples based on a particular element:'''
fruits = [('apple', 10), ('banana', 5), ('orange', 8)]
fruits.sort(key=lambda x: x[1])
print(fruits)  # Output: [('banana', 5), ('orange', 8), ('apple', 10)]

'''In this example, the sort method is used to sort a list of tuples based on the second element of each tuple. The key parameter of the sort method takes a lambda function that returns the second element (x[1]) of each tuple. The list is then sorted based on this lambda function.'''

'''Filtering a list based on a condition:'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

'''Here, the filter function is used to create a new list even_numbers containing only the even numbers from the original list. The lambda function checks if a number is divisible by 2 (x % 2 == 0) and returns True if it is an even number.

Lambda functions are particularly useful in scenarios where defining a separate function would be too cumbersome or unnecessary. They can be used in many other scenarios as well, such as mapping, reducing, or transforming data.'''