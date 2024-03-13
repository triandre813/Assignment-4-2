# This program calculates an employee's productivity bonus.

# Prompt user for employee's name and productivity data
employee_name = input("Enter employee's name: ")
num_shifts = int(input("Enter number of shifts worked: "))
num_transactions = int(input("Enter number of transactions: "))
dollar_value = float(input("Enter dollar value of transactions: "))

# Calculate productivity score
productivity_score = (dollar_value / num_transactions) / num_shifts

# Determine bonus based on productivity score
if productivity_score <= 30:
    bonus = 50.00
elif 31 <= productivity_score <= 69: 
  bonus = 75.00
elif 70 <= productivity_score <= 199:
  bonus = 100.00
else:
  bonus = 200.00

# Output employee's name and bonus
print("Employee Name:", employee_name)
print("Employee Bonus: $" + str(bonus))