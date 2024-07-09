'''Transforming:
The filter() function takes a function object and an iterable and creates a new list.
As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True.

The syntax is:
filter(function, iterable(s))
'''
fruits = ["Apple", "Orange", "Banana", "Pear"]
filter_objects = list(filter(lambda s: s[0] == 'A', fruits))
print(filter_objects)
#['Apple']

# Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 !=0, numbers))
print(result) # Output: [1, 3, 5]

# Square each number in a list
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)  # Output: [1, 4, 9, 16, 25]

names = ["John Doe", "Alice Smith", "Bob Ford", "Jake Lee"]
initials = list(map(lambda name: "".join([n[0] for n in name.split()]), names))
print(initials)
reversed_words = list(map(lambda word: word[::-1], names))
print(reversed_words)