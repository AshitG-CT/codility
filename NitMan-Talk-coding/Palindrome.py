''' Palindrome number : nitin -- nitin, 1234321
A. By Using split method
'''
# String -- Best practice
def palindrome(s):
    temp = s[::-1]
    print('temp value: ', temp)
    if s == temp:
        print("Yes")
    else:
        print("No")

palindrome("liril") ## Yes

# By using indexing / using for loop
def palindrome2(s):
    n = len(s)
    print('length n is: ', n)
    for i in range(n):
        print(f's[{i}]: ', s[i])
        if s[i] != s[n-i-1]:
            return False
    return True

print(palindrome2("nitin"))

# By using Inbuilt function : reserved and join
def palindrome3(s):
    # reverse_s = reversed(s)
    # print(reverse_s)
    # for i in reverse_s:
    #     print(i)
    temp = ''.join(reversed(s))
    print(temp)
    # print(s)
    if s == temp:
        return True
    else:
        return False

print(palindrome3("dad"))

# By using while loop
def palindrome4(s):
    n = len(s)
    first = 0
    last = n-1
    while(first < last):
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True

print(palindrome4("nitin"))

# Palindrome By split method -- not a good metod
def palindrome5(s):
    s = str(s)
    temp = s[::-1]
    if s == temp:
        return True
    else:
        return False

s = 123454321
print(palindrome5(s))

# By using while loop
def palindrome6(n):
    temp = n
    rev_n = 0
    while (temp > 0):
        digit = temp % 10
        print('Digit: ', digit)
        print('Before rev_n: ', rev_n)
        rev_n = rev_n*10 + digit
        print('After rev_n: ', rev_n)
        # rev_n = 0*10 + 6 = 6
        temp = temp // 10 ## 145
        print('Temp: ', temp)
    if n == rev_n:
        return True
    else:
        return False

n = 123454321
print(palindrome6(n))
