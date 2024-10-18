# A program for printing detailed information.

employee = "Mr. Jordany Wick, born on 1998-10-19"


name = employee[4:11]  
surname = employee[12:16]  
dob = employee[-10:]  
initials = f'{employee[4]}{employee[12]}' 


print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {dob}')
print(f'Initials: {initials}')