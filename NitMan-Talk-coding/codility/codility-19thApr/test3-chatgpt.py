'''
You are given a list of all the transactions on a bank account during the year 2020. the Account was empty at the beginning of the year (the balance was 0).
Each transaction specifies the amount and the date it was executed. If the amount is negative (less than 0) then it was a card payment, otherwise it was an incoming transfer (amount at least 0). The date of each transaction is in YYYY-MM-DD format: for example. 2020-05-20 represents 20th May 2020.
Additionally, there is a free for having a card (omitted in the given transation list), which is 5 per month. This fee is deducted from the account balance at the end of each month unless there were at least three payments made by card for a total cost of at least 100 within that month.
Your task is to compute the final balance of the account at the end year 2020.
Write a function:
def solution(A, D)
that, give an array A of N integers representing transation amounts and an array D of N strings representing transaction dates, returns the final balane of the account at the end of the year 2020. Transaction number K (for K within the range [0...N-1]) was executed on the date represented by D[K] for amount A[K].
Examples:
1. given A=[100, 100, 100, -10] and D=["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"], the function should return 230. Total income was equal to 100+100+100+-10=290 and the fee was paid every month, so 290-(5*12) = 230
2. Given A=[180, -50, -25, -25] and D=["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"], the function should return 25. The income was equal to 180, the expenditure was equal to 100 and the fee was applied in every mont except January: 180-100-(5*11) = 25.
3. Given A=[1, -1, 0, -105, 1] and D=["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"], the function should return -164. The fee is paid every month 1-1+0-105+1-(5*12)=-164. Note that in April, even though the total cose of card payments was 106 (more than 100), there were only two payments made by card, so the fee was still applied. A transaction of value 0 is considered a positive, incoming transfer.
4. Given A=[100, 100, -10, -20, -30], D=["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"], the function should return 80.
5. Given A=[-60, 60, -40, -20], D=["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"], the function should return -115.

Assume that:
    - n is an integer within the range [1..100];
    - each element of array A is an integer within the range [-1,000..1,000];
    - D contains strings in YYYY-MM-DD format, representing dates in the range 2020-01-01 to 2020-12-31.
'''

from collections import defaultdict

def solution(A, D):
    transactions = defaultdict(int)
    monthly_fees = 0
    total_income = 0
    
    for i in range(len(A)):
        date = D[i]
        amount = A[i]
        year, month, day = map(int, date.split('-'))
        
        if amount < 0:
            transactions[(year, month)] += amount
        else:
            total_income += amount
    print('transactions : ', transactions)
    for key in transactions.keys():
        if transactions[key] < -100:
            monthly_fees += 5
        elif transactions[key] < -2 * 100:
            monthly_fees += 2 * 5
        elif transactions[key] < -3 * 100:
            monthly_fees += 3 * 5
    print('total_income : ', total_income)
    print('monthly_fees : ', monthly_fees)
    total_balance = total_income + sum(transactions.values()) - monthly_fees
    return total_balance

# Test cases
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"])) # Output: 230
# print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"])) # Output: 25
# print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"])) # Output: -164
# print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"])) # Output: 80
# print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"])) # Output: -115
