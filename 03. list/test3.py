# Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Find Wonder Woman's index
wonder_woman_index = justice_league.index("Wonder Woman")

# Remove Wonder Woman from her current position
wonder_woman = justice_league.pop(wonder_woman_index)

# Insert Wonder Woman at the beginning of the list
justice_league.insert(0, wonder_woman)

# Print the updated list with Wonder Woman as the leader
print("Justice League (Wonder Woman as leader):", justice_league)
