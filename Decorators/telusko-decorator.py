def div(a, b):
    print(a/b)

def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner

div = smart_div(div)
## with smart_div decorator 2.0
div(2, 4) 
## default output: 0.5