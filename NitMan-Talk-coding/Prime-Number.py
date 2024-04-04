'''Prime number: 2 3 5 7 11 13 17 19
# 1. To check if the number is a prime number or not
'''
# Using flag
def prime_number(n):
    flag = False
    if n>1:
        for i in range(2, ((n//2)+1)): ## Remember it for value of n is -- 4 (n//2+1)
            if n%i == 0:
                flag = True
                break
        
    if flag:
        return 'No! It\'s not a prime number'
    else:
        return 'Yes It\'s a prime number' 

print(prime_number(17))
# Contain for 4 is a special condition
# Using for-else -- best Method
def prime_number2(n):
    if n>1:
        for i in range(2, n//2+1):
            if n%i == 0:
                print('No! It\'s not a prime number')
        else:
            print('Yes! It\'s a prime number')
    else:
        print('Yes! It\'s a prime number')
prime_number2(13)


## Using for-else get all prime numbers in range
def prime_number3(start, end):
    for n in range(start, end):
        if n>1:
            for i in range(2, n//2+1):
                if n%i == 0:
                    break
            else:
                print(n)

prime_number3(1, 100)