'''Character Occurence
1. Least repeating character in a string -- best method
'''
def least_char_occurence(s):
    ch = {}
    for i in s:
        if i in ch:
            # print('ch[i] : ', ch[i])
            ch[i] = ch[i]+1
        else:
            ch[i] = 1
    # To print no of occurence of all char
    print(ch)
    result = min(ch, key=ch.get)
    print(result)

s = "aabbccdeeessdda"
least_char_occurence(s)
# {'a': 3, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 's': 2}
# b

# 2. Using inuild function counter
from collections import Counter
s = "aabbccdeeessdda"
ch = Counter(s)
print(ch)
result = min(ch, key=ch.get)
print(result)

# 3. Count of any particular element
# By using count (for string, number, list)
l = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 2, 6, 7]
print('Count of 4: ',l.count(4))

s = 'aabbcccdeeessddaaaaaaa'
print('Count of a: ', s.count('a'))

# 4. Without using count/ using dict
# using dict - Best method
def count_char_occurence(str, search_char):
    char = {}
    for index in str:
        if index in char:
            char[index] = char[index]+1
        else:
            char[index] = 1

    print('All character count: ', char)
    try:
        print(f'{search_char} count is: ', char[search_char])
    except:
        print(0)

str = 'aabbcccdeeessddaaaaaaa'
count_char_occurence(str, 'b')
count_char_occurence(str, 'm')


# 5. Count of all elements
print("Count of all element: ")
# Using dictionary -- best method
def least_char_occurence2(s):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i]+1
        else:
            ch[i] = 1
    print(ch)

str = 'aabbcccdeeessddaaaaaaa'
least_char_occurence2(str)