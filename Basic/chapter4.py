'''String: '''
value = 4*20
print('The value is {value}'.format(value=value))

'''In f-string'''
print(f'The value is {value}')

# range(start, stop, step)
def fibonacci(n):
    sequence = []
    if n <= 0:
        sequence
    elif n == 1:
        sequence.append(0)
    elif n == 2:
        sequence.extend([0, 1])
    else:
        sequence.extend([0, 1])
        for n in range(2, 10):
            print('Range ******** ', n)
            fibonacci = sequence.append(sequence[n-1] + sequence[n-2])
            print(fibonacci)
    return sequence

print(fibonacci(10))