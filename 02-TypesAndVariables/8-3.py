# A program that prints your height both in cm and in feet and inches.


cm = float(input('Enter your height in cm: '))


cm_per_inch = 2.54
inches_per_foot = 12


total_inches = cm / cm_per_inch


feet = int(total_inches // inches_per_foot)


inches = total_inches % inches_per_foot


print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.1f} inches.')