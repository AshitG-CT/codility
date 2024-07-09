# Question 8: Write a Python program to sort a list of elements using the bubble sort algorithm.
# https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac
def bubble_sort(elements):
    n = len(elements)
    for i in range(n-1):
        for j in range(n-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

# Test the function
nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)