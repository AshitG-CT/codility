# Second larget number in a list
# Using for loop -- best method
def second_hightest_number(n):
    if n[0]>n[1]:
        first = n[0]
        second = n[1]
    else:
        first = n[1]
        second = n[0]

    for i in range(2, len(n)):
        if n[i]>first:
            second = first
            first = n[i]
        elif n[i]>second and first!=n[i]: ## remember first!=n[i] for duplicate
            second = n[i]
    return second

l = [10, 20, 30, 4, 100, 22, 666, 666]
print(second_hightest_number(l))

# Using reverse sort
def second_hightest_number2(lst):
    lst.sort(reverse=True)
    print(lst[1])

lst = [10, 20, 30, 4, 100, 22, 666]
second_hightest_number2(lst)


## Get nth largest number
def second_hightest_number3(lst, n):
    lst.sort(reverse=True)
    print(f'{n}th highest num: ', lst[n-1])

lst = [10, 20, 30, 4, 100, 22, 666]
second_hightest_number3(lst, 3)

## To get the second largest number from a list that may contain duplicate values in Python, you can use the following code:
def second_largest(numbers):
    # remove duplicate numbers
    unique_number = set(numbers)
    print('Unique number in set: ', unique_number)
    if len(unique_number) < 2:
        # If there are less than two unique numbers, return None
        return None
    # Sort the unique numbers
    sorted_numbers = sorted(unique_number)

    # Return the second largest number
    return sorted_numbers[-2]
list = [5, 1, 6, 2, 8, 3, 8, 2, 5, 9, 1, 5, 7, 9]
# printing the original list
print('The given list is: ', list)
list1 = second_largest(list)
# printing the second largest number in the list
print('The second largest number in the given list is:', list1)

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
# [5, 1, 6, 2, 8, 3, 9, 7]
