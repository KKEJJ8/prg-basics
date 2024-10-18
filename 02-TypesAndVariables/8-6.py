# A program that reads an integer number from the keyboard
# and prints it as a binary and hexadecimal number.


number = int(input('Enter number: '))


binary_number = bin(number)
hexadecimal_number = hex(number)


print(f'Binary number: {binary_number}')
print(f'Hexadecimal number: {hexadecimal_number}')