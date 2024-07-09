## Snehal's answer
from collections import defaultdict

def solution(A,D):
    balance = 0
    fees = [0] * 12
    payments = [0] * 12
    for amount, date in zip(A,D):
        year, month, _ = map(int, date.split('-'))
        balance += amount
        if amount < 0:
            fees[month - 1] += abs(amount)
            payments[month -1] += 1
    for i in range(12):
        if fees[i] < 100 or payments[i] <3:
            balance -= 5
    return balance            

print(solution([100,100,100,-10],["2020-12-31","2020-12-22","2020-12-03","2020-12-29"]))  #output:230 
print(solution([180,-50,-25,-25],["2020-01-01","2020-01-01","2020-01-01","2020-01-31"]))  # output:25
print(solution([1,-1,0,-105,1], ["2020-12-31","2020-04-04","2020-04-04","2020-04-14","2020-07-12"])) #output:-164 
print(solution([100,100,-10,-20,-30],["2020-01-01","2020-02-01","2020-02-11","2020-02-05","2020-02-08"])) # output:80
print(solution([-60,60,-40,-20],["2020-10-01","2020-02-02","2020-10-10","2020-10-30"])) # output:-115