# The car has three driving modes: Auto (A), Manual (M), and Eco (E).
# Each has an average fuel consumption in liters per 100 km.

# Get the driving mode and distance from the user
driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

# Determine the fuel consumption rate based on the driving mode
if driving_mode == 'A':
    fuel_consumption = 7  # liters per 100 km for Auto
elif driving_mode == 'M':
    fuel_consumption = 9  # liters per 100 km for Manual
elif driving_mode == 'E':
    fuel_consumption = 6  # liters per 100 km for Eco
else:
    fuel_consumption = 0  # Invalid mode

# Calculate total fuel consumption
total_consumption = (fuel_consumption * distance) / 100

print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')