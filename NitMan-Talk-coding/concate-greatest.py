'''find the Greatest possible number by concatenating it from array ie if you have array [3, 23, 4, 6] the output should be [64323]'''
from functools import cmp_to_key

def compare(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return 1
    else:
        return -1

def find_greatest_number(arr):
    arr.sort(key=cmp_to_key(compare), reverse=True)
    return int(''.join(map(str, arr)))

# Example
arr = [3, 23, 4, 6]
result = find_greatest_number(arr)
print(result)
# 64323

# ---------------------------
def compare(a, b):
    # print('a: b: ', a, b)
    # print('a+b: ', a+b)
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def concatenate_largest_number(arr):
    arr_str = [str(x) for x in arr]
    print('arr_str: ', arr_str)
    arr_str.sort(key=cmp_to_key(compare))
    return int(''.join(arr_str))

arr = [3, 23, 4, 6]
result = concatenate_largest_number(arr)
print(result)
# ---------------------------------
'''cmp_to_key() uses a key to compare elements
It is built into functools module, thus functools has to be imported first in order to use the function
Used with tools that accept key functions such as min(), max(), sorted() etc.
Takes only one argument which strictly should be a callable
This function returns a special key that can be used to compare elements'''
def mycmp(a, b):
    print("Compairing  ", a, "and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

print(sorted([45, 78, 813, 2], key=cmp_to_key(mycmp)))
'''
Compairing   78 and  45
Compairing   813 and  78
Compairing   2 and  813
Compairing   2 and  78
Compairing   2 and  45
[2, 45, 78, 813]'''