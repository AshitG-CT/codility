'''
https://app.codility.com/programmers/trainings/5/parking_bill/
You parked your car in a parking lot and want to compute the total cost of the ticket. The billing rules are as follows:

The entrance fee of the car parking lot is 2;
The first full or partial hour costs 3;
Each successive full or partial hour (after the first) costs 4.
You entered the car parking lot at time E and left at time L. In this task, times are represented as strings in the format "HH:MM" (where "HH" is a two-digit number between 0 and 23, which stands for hours, and "MM" is a two-digit number between 0 and 59, which stands for minutes).

Write a function:

def solution(E, L)

that, given strings E and L specifying points in time in the format "HH:MM", returns the total cost of the parking bill from your entry at time E to your exit at time L. You can assume that E describes a time before L on the same day.

For example, given "10:00" and "13:21" your function should return 17, because the entrance fee equals 2, the first hour costs 3 and there are two more full hours and part of a further hour, so the total cost is 2 + 3 + (3 * 4) = 17. Given "09:42" and "11:42" your function should return 9, because the entrance fee equals 2, the first hour costs 3 and the second hour costs 4, so the total cost is 2 + 3 + 4 = 9.

Assume that:

strings E and L follow the format "HH:MM" strictly;
string E describes a time before L on the same day.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

Copyright 2009–2024 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
from datetime import datetime
import math

def car_cost(enter, left):
    entrance_fees = 2
    first_full_hr = 3
    enter_time = datetime.strptime(enter, "%H:%M")
    left_time = datetime.strptime(left, "%H:%M")
    # print(enter_time.time().__format__("%H:%M"))
    # print(left_time.time().__format__("%H:%M"))
    delta = enter_time - left_time
    # print('delta in sec: ', delta.total_seconds())
    # print('delta in min: ', (delta.total_seconds())/(60))
    # print('delta in hr: ', (delta.total_seconds())/(60 * 60))

    total_hr = (delta.total_seconds())/(60 * 60)
    total_hr = abs(math.floor(total_hr))
    # print('total_hr : ', total_hr-1)

    # The first full or partial hour costs 3
    total_cost = ((total_hr-1)*4)+entrance_fees+first_full_hr
    # print('total_cost ** ', total_cost)
    return total_cost

print(car_cost("10:00", "13:21"))
print(car_cost("09:42", "11:42"))