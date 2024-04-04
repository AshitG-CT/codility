# Armstrong Number
# A no that is equal to the sum of cubes of its digit
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1+125+27 = 153
# 371 = 3*3*3 + 7*7*7 + 1*1*1 = 27+343+1 = 371

def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp%10
        sum = sum+(digit**3)
        temp = temp//10
    
    if n == sum:
        print("Yes")
    else:
        print("No")
n = 371
armstrong(n)

## Print list of armstrong number for a particular interval
def armstrong2(start, end):
    for n in range(start, end):
        sum = 0
        temp = n
        while temp>0:
            digit = temp%10
            sum = sum+(digit**3)
            temp = temp//10

        if n == sum:
            print(n)

armstrong2(0, 500)

## Sum of digit
def sum_of_digit(n):
    sum = 0
    temp = n
    if n>9:
        while temp > 0:
            digit = temp%10
            print('digit : ', digit)    # 5
            sum = sum+digit
            print('sum: ', sum) # 5
            temp = temp//10
            print('temp: ', temp)   # 1234

    else:
        sum = n
    return sum

print(f"Sum of digit: ", sum_of_digit(12345))