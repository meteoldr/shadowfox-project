countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Get user input for two cities
city1 = input("Enter the first city: ").capitalize()
city2 = input("Enter the second city: ").capitalize()

# Check if both cities belong to the same country
same_country = False
for country, cities in countries.items():
  if city1 in cities and city2 in cities:
    same_country = True
    break  # Exit the loop after finding a match

if same_country:
  print(f"Both cities, '{city1}' and '{city2}', are in {country}.")
else:
  print(f"The cities '{city1}' and '{city2}' do not belong to the same country.")
