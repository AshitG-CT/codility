'''
Map() Function
The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
The syntax is:
map(function, iterable(s))
Certainly! Here are some additional examples of mapping, reducing, and transforming data using lambda functions in Python:'''
# '''Mapping a list of numbers to their squares:'''
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print('result  : ', result)  # Output: [2, 4, 6, 8, 10]

## By using for loop - comperhension
result2 = [i*2 for i in numbers]
print('result2 : ', result2)

# Convert a list of strings to uppercase
words = ["hello", "world", "lambda"]
result = list(map(lambda x: x.upper(), words))
print(result)  # Output: ['HELLO', 'WORLD', 'LAMBDA']

# Create a list using range 1-15 and get squar
# range_list = list(range(1, 16))
range_list = [*range(1, 16)]
print('Range 1 to 15: ', range_list)
result_squar = list(map(lambda x: x ** 2, range_list))
print('Squar list: ', result_squar)


fruits = ["Apple", "Orange", "Banana", "Pear"]
map_object = map(lambda s: s[0] == 'B', fruits)
print(list(map_object))
# [False, False, True, False]