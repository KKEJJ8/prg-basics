import math

def calculate_distance_to_horizon(height):
    return 3.57 * math.sqrt(height)


height = 1.86
distance = calculate_distance_to_horizon(height)
print(f"The distance to the horizon from a height of {height} meters is: {distance:.2f} km")


hotel_window_height = 20
distance_hotel = calculate_distance_to_horizon(hotel_window_height)
print(f"The distance to the horizon from a height of {hotel_window_height} meters is: {distance_hotel:.2f} km")