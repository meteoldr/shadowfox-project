justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Choose who to insert (change "Green Lantern" to "Superman" if preferred)
separator = "Green Lantern"

# Find the indices of Aquaman and Flash
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# Insert the separator between them (depending on their order)
if aquaman_index < flash_index:
    justice_league.insert(aquaman_index + 1, separator)
else:
    justice_league.insert(flash_index + 1, separator)

# Print the modified Justice League list
print(justice_league)
