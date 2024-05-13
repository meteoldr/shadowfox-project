# Define pi 
pi = 3.14

# Pond radius
radius = 84

# Calculate pond area
pond_area = pi*radius*radius

# Water per square meter (given in liters)
water_per_square_meter = 1.4

# Calculate total water in the pond (round down to whole liters)
total_water = int(pond_area * water_per_square_meter)

# Print results
print("Pond Area:", pond_area, "square meters")
print("Total Water in the Pond:", total_water, "liters")
