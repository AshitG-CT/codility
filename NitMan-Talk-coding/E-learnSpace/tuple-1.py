t1 = ("tuple", False, 3.2, 1)
print(t1)
t1 = (4, 6, 2, 8, 3, 1)
print(t1)
t1 = t1 + (9,)
print(t1)
# adding item at a specfic index
t1 = t1[:5]+(15,20,25)+t1[:5]
print(t1)
# Converting into list
l1 = list(t1)
print(l1)
l1.append(89)
t1 = tuple(l1)
print(t1)

tup = ('e','x','e','r','c','i','s','e')
str1 = ''.join(tup)
print(str1)
# exercise

t1 = ((2, 'x'), (3, 'y'))
print(dict((a, b) for a,b in t1))
# {2: 'x', 3: 'y'}

t2 = (100, 200, 300)
print('This is a tuple {0} '.format(t2))
# This is a tuple (100, 200, 300)

num = [10, 20, 30, 40, (10, 20), 50]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr+=1
print(ctr)