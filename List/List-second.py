## https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
## To get the second largest number from a list that may contain duplicate values in Python, you can use the following code:
list = [5, 1, 6, 2, 8, 3, 8, 2, 5, 9, 1, 5, 7, 9]
# printing the original list
print('The given list is: ', list)

# remove duplicate numbers
unique_number = set(list)
print('Unique number in set: ', unique_number)

list1 = sorted(unique_number, reverse=True)
print('The sorted list is: ', list1)

# printing the second largest number in the list
print('The second largest number in the given list is:', list1[1])

## To get the second largest number from a list (without duplicate numbers)in Python, you can use the following code:
# python program to find second largest number in the given list
print('----------------------------------')
# Initializing the list
list = [2, 1, 8, 7, 3, 0]
 
# printing the original list
print('The given list is:', list)

list1 = []
list1 = sorted(list, reverse=True)
print('The sorted list is: ', list1)

# printing the second largest number in the list
print('The second largest number in the given list is:', list1[1])