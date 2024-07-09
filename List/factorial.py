def factorial(n):
    if n < 0:
        return "Error: Input must be a non-negative number"

    result = 1
    for i in range(1, n+1):
        result *=i

    return result

print('Factorial of 5: ', factorial(5))
print('Factorial of 0: ', factorial(0))
print('Factorial of -3: ', factorial(-3))