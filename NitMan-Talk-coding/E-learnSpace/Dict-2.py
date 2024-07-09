dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:40, 6:60}
dict4 = {}
for d in (dict1, dict2, dict3):
    dict4.update(d)
print(dict4)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 40, 6: 60}

n = int(input('Input a num: '))
d = dict()
for x in range(1, n+1):
    d[x] = x*x
print(d)
# Input a num: 4
# {1: 1, 2: 4, 3: 9, 4: 16}

num = {'n1': [9,3,1], 'n2':[0,2,4], 'n3':[9,45,21]}
sorted_d = {x:sorted(y) for x, y in num.items()}
print(sorted_d)
# {'n1': [1, 3, 9], 'n2': [0, 2, 4], 'n3': [9, 21, 45]}