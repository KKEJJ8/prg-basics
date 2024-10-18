# Vehicle registration numbers in Krakow start with the letters KR or KK.
# This program checks if a vehicle registration number is from Krakow.

car_number = input('Enter car registration number: ')


is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"


print(f'Car is from Krakow: {is_krakow}')