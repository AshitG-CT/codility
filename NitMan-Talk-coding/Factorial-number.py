'''Factorial number
 - for loop
 2nd case - 145!= 1!+4!+5! = 1+24+120 = 145
 Print number from 1 to 1 lakh where
 # the 'sum' of the 'factorial of each digit equals to the 'actual number'
 for example
 145! = 1! + 4! + 5! = 1+24+120 = 145
'''
def factorial(n):
    facto = 1
    for i in range(1, n+1):
        facto = facto*i     # facto*=i
    return facto

print(factorial(5))
print(factorial(6))

# whether number follows the case
def sum_of_facto(n):
    temp = n
    sum = 0
    while (temp>0):
        digit = temp%10
        temp = temp//10
        facto = factorial(digit)
        sum = sum + facto
    if sum == n:
        print('Yes')
    else:
        print('No')

sum_of_facto(144)
sum_of_facto(145)

# Print list of numbers that follows the case within interval:
print("list of number that follows the case within interval")
def sum_of_facto2(start, end):
    for n in range(start, end):
        temp = n
        sum = 0
        while (temp>0):
            digit = temp%10
            temp = temp//10
            facto = factorial(digit)
            sum = sum + facto
        if sum == n:
            print(n)

sum_of_facto2(1, 200000)

# Udemy - Using recursion method
def factorial2(number):
    if number == 1:
        return 1
    else:
        return number* factorial2(number-1)
print(factorial2(4))
# 24