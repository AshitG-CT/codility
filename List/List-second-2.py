## https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
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

## To get the second largest number from a list (without duplicate numbers)in Python, you can use the following code:
# python program to find second largest number in the given list
print('----------------------------------')
# Initializing the list
list = [2, 1, 8, 7, 3, 0]
# printing the original list
print('The given list is:', list)

def secondmax(arr):
    sublist = []
    sublist = [x for x in arr if x < max(arr)]
    return max(sublist)

# printing the second largest number in the list
print('The second largest number in the given list is:', secondmax(list))