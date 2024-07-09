list_2 = range(1, 24)
print(list_2)

list_125 = [*range(1, 26)]
print('number 1 to 25', list_125)

numbers = range(1, 25)
print('Range list: ', list(numbers))

squar_list = list(map(lambda x: x * 2, list(range(1, 25))))

print('Squar list: ', squar_list)