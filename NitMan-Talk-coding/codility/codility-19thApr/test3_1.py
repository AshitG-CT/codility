import datetime

def solution(A, D):
    total_income = 0
    total_expense = 0
    card_payments = {}
    
    for i in range(len(A)):
        date = datetime.datetime.strptime(D[i], "%Y-%m-%d")
        month = date.month
        
        if A[i] >= 0:
            total_income += A[i]
        else:
            total_expense += abs(A[i])
            card_payments[month] = card_payments.get(month, 0) + abs(A[i])
    
    total_fee = 0
    
    for month in range(1, 13):
        if month in card_payments and card_payments[month] >= 100:
            continue
        total_fee += 5
    
    final_balance = total_income - total_expense - total_fee
    
    return final_balance

# Test cases
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"])) # Output 230
print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"])) # Output 25
print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"])) # Output -164
print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"])) # Output 80
print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"])) # Output -115
