'''
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.
Test Data
Sample input:
12
17
59

Expected output: 13:16

Sample input:
23
58
642

Expected output: 10:40

Sample input:
0
1
2939

Expected output: 1:0

Code
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
hour = int(input("Starting time (hours): "))'''

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# # Calculate end time
# end_hour = (hour + ((mins + dura) // 60)) % 24
# end_min = (mins + dura) % 60

# print(f"{end_hour}:{end_min:02}")
# print(123+0.0)
# x = 2
# y = 4
# x = x // y
# print(x)
# y = y // x
# print(y)

print(1 // 2 * 3)
y = 2 + 3 * 5.
print(y)
x = int(input())
y = int(input())
print(x+y)
# 
'''
Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
'''
income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if income <= 85528:
    tax = round((income * 0.18) - 556.02)
# if income > 85528:
#     tax = income - 14839
else:
    tax = round(14839.02 + 0.32 * (income - 85528))
    
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
