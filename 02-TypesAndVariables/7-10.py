# A program that enables a user to challenge a computer by guessing a dice roll.

import random

# COMPUTER TURN: The computer rolls the dice (1 to 6)
computer = random.randint(1, 6)

# USER TURN: The user tries to guess the number
you = int(input('Guess the number on the dice (1 to 6): '))

# Check if the user guessed correctly
result = you == computer

# Print the results
print(f'The computer rolled: {computer}')
print(f'You won: {result}')