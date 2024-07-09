def decorator_func(func):
    def wrapper_func():
        print("Wrapper_func Worked")    ## 2
        return func()
    print("decorator_func worked")  ## 1 
    return wrapper_func

def show():
    print("Show Worked")    ## 3

decorator_show = decorator_func(show)
decorator_show()

## alternative
# def display():
#     print('display worked')
# decorator_display = decorator_func(display)
# decorator_display()
@decorator_func
def display():
    print('display worked')
display()
'''output:
decorator_func worked
Wrapper_func Worked
Show Worked
'''
'''
decorator_func worked
Wrapper_func Worked
display worked
'''