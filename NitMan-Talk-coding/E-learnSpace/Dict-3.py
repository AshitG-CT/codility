# count no of occurences of each letter in the given string
word = input("Enter some word: ")
d = {}
for x in word:
    d[x] = d.get(x, 0)+1
print(d)
# not print in dictionary fore
for k, v in d.items():
    print(k, "occurred ", v, "times")



# count no of occurences of each vowel
word = input("Enter some word: ")
vowels = {'a', 'e', 'i', 'o','u'}
d = {}
for x in word:
    if x in vowels:
        d[x] = d.get(x, 0)+1

# not print in dictionary fore
for k, v in sorted(d.items()):
    print("{} occurred {} times".format(k, v))