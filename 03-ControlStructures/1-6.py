# Checking whether the number entered from the keyboard is even or odd
number = int(input('Enter number: '))

# Check if the number is even or odd
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')