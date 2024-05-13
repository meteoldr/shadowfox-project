def calculate_bmi(height, weight):
  bmi = weight / (height * height)
  return bmi
def determine_bmi_category(bmi):
  if bmi >= 30:
    category = "Obesity"
  elif bmi >= 25:
    category = "Overweight"
  elif bmi >= 18.5:
    category = "Normal"
  else:
    category = "Underweight"
  return category
# Get user input for height and weight
try:
  height = float(input("Enter height in meters: "))
  weight = float(input("Enter weight in kilograms: "))
except ValueError:
  print("Error: Please enter valid numbers for height and weight.")
else:
  # Calculate BMI and determine category
  bmi = calculate_bmi(height, weight)
  category = determine_bmi_category(bmi)
 # Print the results
  print(f"Your BMI is: {bmi:.2f}")
  print(f"BMI Category: {category}")
