# Udemy - Remove duplicate numbers
def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

ids = [5, 1, 6, 2, 8, 3, 8, 2, 5, 9, 1, 5, 7, 9]
result2 = remove_duplicates(ids)
print(result2)
# Output: [5, 1, 6, 2, 8, 3, 9, 7]

# NitMan - Sort number without using sort keyword
def sort_list(list1):
    # list1 = remove_duplicates(list1)
    num_length = len(list1)
    for i in range(num_length):
        for j in range(i+1, num_length):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    # print('Sorted list: ', list1)
    return list1

print('Sorted List: ', sort_list(ids))
print('Sort list remove duplicate:', sort_list(result2))

## Sort a dictionary By using dict comprehension
dict1 = {575: 'Apple', 876: 'Mango', 132: 'Grapes', 782: 'Banana'}
d = sorted(dict1.keys())
dict2 = {}

for i in d:
    dict2[i] = dict1[i]

print('sort by value: ',dict2)

dict3 = {key:value for key, value in sorted(dict1.items(), key=lambda x: x[1])}
print('sort by key: ', dict3)