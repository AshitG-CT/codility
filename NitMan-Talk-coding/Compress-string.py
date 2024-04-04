# Compress String
# aabbccddeeeee = a2b2c2d2e4

# Input - aabbccaaaafffeiii
# Output - a2b2c2a4f3e1i3

# By Using for loop -- best method
def compress(s):
    n = len(s)
    new_s = ''
    count = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            new_s = new_s + s[i] + str(count)
        #  new_s += (s[i]+str(count))
            count = 1
    new_s = new_s + s[n-1] + str(count)     ## important
    return new_s

s = 'aabbccaaaafffeiii'
print(compress(s))


# By using while loop
def compress2(s):
    n = len(s)
    i = 0
    new_s = ''
    while (i<n-1):
        count = 1
        while (i<n-1 and s[i] == s[i+1]):
            count +=1
            i+=1
        i+=1
        new_s = new_s + s[i-1]+str(count)
    return new_s

s = 'aabbccaaaafffeiii'
print(compress2(s))

# Find the maximum repeated character in a string without having on 2 complexity
s = 'itininiytnnhhn'
ch = {}
for i in s:
    if i in ch:
        ch[i] +=1
    else:
        ch[i] = 1
print(ch)

max_char = max(ch, key=ch.get)
print(max_char, ch[max_char])