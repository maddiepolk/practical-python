# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_count = 0
extra_payment_start_month = 61 # could also set these up to be input() but sticking with static values here
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month_count >= extra_payment_start_month and month_count <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        month_count += 1
    else: 
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        month_count += 1
    print(f'{month_count}, ${total_paid:0.2f}, ${principal:0.2f}') # Exercise 1.10 Modify the program to print out a table showing the month, total paid so far, and the remaining principal.

print('Total paid', total_paid)

# Exercise 1.8 - Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
# while principal > 0:
#     while month_count < 12: 
#         principal = principal * (1+rate/12) - payment - 1000
#         total_paid = total_paid + payment + 1000
#         month_count += 1
#     principal = principal * (1+rate/12) - payment
#     total_paid = total_paid + payment
#     month_count += 1
#     print(month_count, payment, principal, total_paid)


# Exercise 1.11 (Bonus) - While you’re at it, fix the program to correct for the overpayment that occurs in the last month.
# MP Note - not sure how to do this exercise

# Exercise 1.12 
# Can you explain this behavior?
# >>> bool("False")
# True

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.