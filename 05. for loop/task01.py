import random
# Simulate rolling a die 20 times
num_rolls = 20
rolls = []
for _ in range(num_rolls):
  roll = random.randint(1, 6)
  rolls.append(roll)

# Count the occurrences of each number
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for roll in rolls:
  counts[roll] += 1

# Count the number of times you rolled a 6 and a 1
consecutive_sixes = 0
for i in range(len(rolls) - 1):
  if rolls[i] == 6 and rolls[i + 1] == 6:
    consecutive_sixes += 1

# Print the results
print("Results of rolling a six-sided die 20 times:")
for num, count in counts.items():
  print(f"  - Rolled {num} {count} times")
print(f"  - Rolled two 6s in a row {consecutive_sixes} times")
