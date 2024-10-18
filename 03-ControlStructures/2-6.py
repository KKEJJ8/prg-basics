# Function to check the number
def check_number(n):
    if n > 0:
        print(f"Number {n} is positive")
    elif n < 0:
        print(f"Number {n} is negative")
    else:
        print("Number is 0")

# List of numbers to check
numbers_to_check = [7, 1, 0, -1, -4]

# Loop through the numbers and check each one
for num in numbers_to_check:
    check_number(num)