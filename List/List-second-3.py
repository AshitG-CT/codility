from functools import reduce
list_125 = [5, 1, 6, 2, 8, 3, 8, 2, 5, 9, 1, 5, 7, 9]
# printing the original list
print('The given list is: ', list_125)
# new_list is a set of list1
new_list = set(list_125)
print('Unique number in set: ', new_list)
new_list.remove(max(new_list))
print('The second largest number in the given list is:', max(new_list))
result = reduce(lambda x, y: x if x > y else y, new_list)
print('Using reduce The second largest number in the given list is:', result)

## Interview quest - get sum of all even number in the list
my_numbers = [1, 2, 3, 4, 5, 6]
def sum_even_number(number):
    total = 0
    for num in number:
        if num % 2 == 0:
            total += num
    return total

even_number = sum_even_number(my_numbers)
print(even_number)