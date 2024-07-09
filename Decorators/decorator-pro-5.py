# https://www.programiz.com/python-programming/decorator
def star(func):
    def inner(*args, **kwargs):
        print('*'* 15)
        func(*args, **kwargs)
        print('*'*15)
    return inner

def precent(func):
    def inner(*args, **kwargs):
        print('%'* 15)
        func(*args, **kwargs)
        print('%'*15)
    return inner

@star
@precent
def printer(msg):
    print(msg)

# star(precent(printer('Hello')))
printer('Hello')