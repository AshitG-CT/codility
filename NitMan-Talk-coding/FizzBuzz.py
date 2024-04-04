# FizzBuzz problem - 3* - Fizz, 5* - Buzz, 15* - FizzBuzz
'''
If number divisible by 3 - print Fizz
If number divisible by 5 - print Buzz
If number divisible by 15 - print FizzBuzz
else print the number
1 - 1
2 - 2
3 - Fuzz
4 - 4
5 - Buzz
6 - Fizz
# ....
# 15 - FizzBuzz
'''

# By using for loop
def fizzbuzz(n):
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:   # i%15 ==0
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

# fizzbuzz(20)


# By using Dictionary
def fizzbuzz2(n):
    d = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, n+1):
        result=''
        for k, val in d.items():
            if i%k == 0:
                print('value: ', val)
                result = result+val
        if not result:
            result = i
        print(result)

fizzbuzz2(15)