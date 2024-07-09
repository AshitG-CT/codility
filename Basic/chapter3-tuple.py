'''Tuple: Immutable sequesces of arbitrary ojebt.
Immutable: Once created the ojebct within them cannot be replaced or removed, and new elements cannot be added, modify'''

e = ()
e
print(type(e))
p = 1, 1, 1, 4, 6, 19
print(p)

def minmax(items):
    return min(items), max(items)

print(minmax([83,33,84,32,85,31,86]))

'''Tuple unpacking: Destructing operation that uppacks data structures into named references'''
lower, upper = minmax([83,33,84,32,85,31,86])
LowerVal = "Lower value: "+ str(lower)
UpperVal = "Upper value: "+ str(upper)
print(LowerVal)
print(UpperVal)
LowerVal = "Lower value: ", lower
UpperVal = "Upper value: ",upper
print(LowerVal)
print(UpperVal)

(a, (b, (c,d))) = (4, (3, (2,1)))
print(a)
print(b)
print(c)
print(d)

j = 'jelly'
b = 'bean'
j, b = b, j
print(j)
print(b)

print(5 in [1, 2, 3, 4, 5])
print(5 not in [1, 2, 3, 4, 5])

'''eval : parse the expression argument and evaluate it as in python'''

print(eval("2 ** 8"))
print(eval('1+2+3'))
print(eval("sum([8, 16, 32])"))
