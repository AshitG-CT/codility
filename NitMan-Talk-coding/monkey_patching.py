'''In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python, we can actually change the behavior of code at run-time.'''
# class A:
#     def func(self):
#         print('func() is called.')

# We use above module (monkey) in below code and change behavior of func() at run-time by assigning different value.
import monkey
def monkey_func(self):
    print('monkey_func() is called.')

# replacing address of "func" with "monkey_func"
monkey.A.func = monkey_func
obj = monkey.A()

# calling function "func" whose address got replaced
# with function "monkey_func()"
obj.func()

# Examples:
# Output :monkey_func() is called.