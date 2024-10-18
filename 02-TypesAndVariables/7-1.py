# People up to and including 26 years of age are exempt from paying taxes in Poland.
# This program checks if the person is exempt from paying taxes.

age = int(input('Enter age: '))
no_tax = age <= 26  

print(f'Exemption from paying taxes: {no_tax}')