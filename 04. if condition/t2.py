countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Get user input for city name
city = input("Enter a city name: ").capitalize()

# Check if the city is in any of the countries' lists
for country, cities in countries.items():
  if city in cities:
    print(f"{city} is in {country}")
    break  # Exit the loop after finding the first match
else:
  print(f"City '{city}' not found in any of the listed countries.")
