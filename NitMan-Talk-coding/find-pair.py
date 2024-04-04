## Find the pair by given number in a list
list1 = [8, 7, 2, 5, 3, 1]
n = len(list1)
k = 10
for i in range(n):
    for j in range(i+1, n):
        if (list1[i] + list1[j]) == k:
            print(list1[i], list1[j])

''' Output:
            8 2
            7 3
'''