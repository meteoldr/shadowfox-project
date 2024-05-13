# Distance (meters)
distance = 490

# Time (minutes)
time_in_minutes = 7

# Convert time to seconds (important for speed calculation)
time_in_seconds = time_in_minutes * 60

# Speed calculation (meters per second)
speed = int(distance / time_in_seconds)

# Print result (rounded down to whole number using int())
print("Speed:", speed, "meters per second")
