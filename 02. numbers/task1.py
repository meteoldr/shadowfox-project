#Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string.
#Print the result. Try to identify the representation used.
def format_string(num, char):
 formatted_string = "The number {num} in octal is {num:o}", format(num=num); return formatted_string
# Call the function and print the result
result = format_string(145, 'o')
print(result)