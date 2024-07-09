'''
A lambda function in Python is a small, anonymous function that can take any number of arguments but can only have one expression. It is defined using the lambda keyword.

Lambda functions are used in Python for creating small, one-time use functions without the need to define a proper function using the def keyword. They are commonly used when a small piece of code needs to be executed inline, without defining a separate function.

Here are a few examples of how lambda functions can be used:

Simple addition:
'''
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
'''In the above example, a lambda function addition is defined with two arguments x and y. The function simply returns the sum of the two arguments. 
The lambda function is then invoked with the values 2 and 3, resulting in the output 5'''

result = (lambda s: s**2)(7)
print(result)   #49
result1 = (lambda x=10, y=20: x+y)(y=50)
print(result1) # 60