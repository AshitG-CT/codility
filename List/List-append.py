'''append(): append method add a single element at the end of a list.
list.append(element)'''

ino_list = [1, 2, 3]
ino_list.append(4)
print('Append list: ', ino_list)
# Append list:  [1, 2, 3, 4]
ing_list = [1, 2, 3]
ing_list2 = [4, 5, 6]
ing_list.append(ing_list2)
print(ing_list) 
# [1, 2, 3, [4, 5, 6]]
'''extend(): extend method is used to add multiple elements to the end of a list. The input can be any iterable e.g (list, tuple, string)
list.extend(iterable)'''
ing_list = [1, 2, 3]
ing_list2 = [4, 5, 6]

print('add list: ', ing_list + ing_list2)
# add list:  [1, 2, 3, 4, 5, 6]

ing_list.extend(ing_list2)
print('Extend list: ', ing_list)
# Extend list:  [1, 2, 3, 4, 5, 6]

'''insert(): insert method is used to add an element at a specific index in the list. All elements after the inserted element will be shifted to the right.'''
my_list = [1, 2, 3]
my_list.insert(2, 6)
print('Insert list: ', my_list)
# Insert list:  [1, 2, 6, 3]