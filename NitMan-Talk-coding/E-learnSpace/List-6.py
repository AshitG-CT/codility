'''print index of an item'''
num = [2,3,4,5,6,23,33]
print(num)
a = int(input("Enter your num: "))
print(num.index(a))

'''to print unique value from the list'''
my_list = [3, 44, 56, 3, 4, 78, 90, 76, 90]
print('Original List: ', my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print('The list of unique values: ', my_new_list)