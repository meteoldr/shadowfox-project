total_jumping_jacks = 100
completed_jacks = 0

while completed_jacks < total_jumping_jacks:
  # Perform 10 jumping jacks (simulation)
  print(f"Perform 10 jumping jacks! (You've done {completed_jacks} so far)")
  completed_jacks += 10

  # Check if user is tired
  is_tired = input("Are you tired? (yes/no) ").lower()

  if is_tired in ("yes", "y"):
    # Ask if user wants to skip remaining sets
    skip_remaining = input("Do you want to skip the remaining sets? (yes/no) ").lower()
    if skip_remaining in ("yes", "y"):
      break  # Exit the loop (workout stopped)

  # Display remaining jumping jacks (if not skipping)
  remaining_jacks = total_jumping_jacks - completed_jacks
  print(f"You have {remaining_jacks} jumping jacks remaining.")

# Print completion message
print(f"You completed a total of {completed_jacks} jumping jacks!")
