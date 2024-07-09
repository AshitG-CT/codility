'''
Generators are iterators which can execute only once. 
Every generator is an iterator.
Generator uses “yield” keyword.
Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
'''
def sqr(n):
    for i in range(1, n+1):
        print("i : ", i)
        print("n : ", n)
        yield i*i
a = sqr(3)

print("The Square are: ")
print('Retrun of 1-a: ', next(a))
print('Retrun of 2-a: ', next(a))
print('Retrun of 3-a: ', next(a))

'''output:
The Square are: 
i :  1
n :  3
Retrun of 1-a:  1
i :  2
n :  3
Retrun of 2-a:  4
i :  3
n :  3
Retrun of 3-a:  9
'''