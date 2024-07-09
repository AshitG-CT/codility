'''zip(): function in python is used to combine two or more iterables (such as lists, tuples or strings) into a single iterable and merges them together.'''

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

zipped = zip(list1, list2)
print(type(zipped))
# for item in zipped:
#     print(item)

mergd_list = list(zipped)
print('mergd_list: ', mergd_list)
# output: mergd_list:  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]