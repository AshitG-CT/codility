'''Decorator: In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.
A Python decorator is a function that takes in a function and returns it by adding some functionality.
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, '''

def hello_decorator(func):
    def inner_function(*args, **kwargs):
        print('Before the function.')
        result = func(*args, **kwargs)
        print('After the Function.')
        return result
    return inner_function

@hello_decorator
def sum_of_numbers(a, b):
    print('Inside the function.')
    return a + b

a, b = 2, 5

print("Sum = ", sum_of_numbers(a, b))
