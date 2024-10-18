# Program for checking clothing sizes

# Prompt the user to enter a size symbol
size = input('Enter size symbol: ')

# Check the entered symbol and print the corresponding size description
if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')