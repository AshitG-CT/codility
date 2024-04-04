## Reverse string 
## "the sky is blue"
## "blue is sky the"

s = "the sky is blue"
l = s.split() # ['the', 'sky', 'is', 'blue']
l = l[::-1]   # ['blue', 'is', 'sky', 'the']
l = ' '.join(l) # blue is sky the
print(l)


def reverseList(lst):
    if not lst:
        return []
    return [lst[-1]] + reverseList(lst[:-1])
    # return lst[::-1]

print(reverseList([1, 2, 3, 4, 5]))
# Output: [5,4,3,2,1]
