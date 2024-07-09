# def chocolate():
#     print('chocolate')
# chocolate()

def chocolate():
    print('chocolate')
 
# this decorator function accepts function as argument
 
def decorator(func):
    # inside the decorator function we have another function
    def wrapper():
        print('Wrapper up side')
        # now here I call the func
        func()
        print('Wrapper down side')
    # now the decorator needs to return this wrapper
    return wrapper
 
# now to call the functions, i first call the decorator and then pass chocolate inside it
# then assign the function back to the previous main function i.e chocolate
# finally call the chocolate function
chocolate = decorator(chocolate)
chocolate()