# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.

# Define the basic salary
basic_salary = 5000

# Define bonus cases: no bonus and 30% bonus
bonus_cases = [0, 0.30]

# Process each case
for bonus in bonus_cases:
    # Check if the employee receives a bonus
    if bonus > 0:
        total_salary = basic_salary + (basic_salary * bonus)
        is_bonus = True
    else:
        total_salary = basic_salary
        is_bonus = False

    # Output the results
    print(f'Basic salary: {basic_salary} PLN')
    print(f'Bonus included? {is_bonus}')
    print(f'Total salary: {total_salary} PLN\n')