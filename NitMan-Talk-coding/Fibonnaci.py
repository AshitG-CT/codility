# Fibonnaci series
# find the fibonnaci series from 0 to nth using while loop

# 0 1 1 2 3 5 8 13 21 .......

# By using while loop
def fibonnaci(n):
    a = 0
    b = 1
    print(a)
    while (b < n):
        print(b)
        # c = a+b
        # a = b
        # b = c
        a, b = b, a+b

# fibonnaci(50)

# By Using Gnerator an infinity fibonnacci series
def fibonnacci_serise():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
f1 = fibonnacci_serise()
# for i in f1:
#     print(i)

print('Using Gnerator: ', next(f1))
print('Using Gnerator: ', next(f1))
print('Using Gnerator: ', next(f1))

# By using for loop
def fibonnaci2(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)

# fibonnaci2(7)

# By using recursion -- best method
def fibonnaci3(n):
    if n<=1:
        return n
    else:
        return (fibonnaci3(n-1) + fibonnaci3(n-2))

n = 10
if n<=0:
    print("Invalid")
else:
    for i in range(n):
        print(fibonnaci3(i))


# Udemy - By using map and lambda function
def fibonnacci4(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        fib_sequence.extend(map(lambda i: fib_sequence[i-1] + fib_sequence[i-2], range(2, n)))
        return fib_sequence
    
fibonnacci_sequence = fibonnacci4(10)
print(fibonnacci_sequence)
# Output:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]