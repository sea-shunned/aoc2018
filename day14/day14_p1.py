# Input
practice_recipes = 793031
# Initial recipe scores
scoreboard = [3, 7]
# Indices for the elves current position
elf1 = 0
elf2 = 1
# Get the required number of practice recipes
while len(scoreboard) < practice_recipes:
    # Turn into string to get each digit
    new_recipes = str(scoreboard[elf1] + scoreboard[elf2])
    # Add them all to the scoreboard
    scoreboard.extend([int(i) for i in new_recipes])
    # Get the new index
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

# Same as above for the extra 10 we need
for i in range(10):
    # Turn into string to get each digit
    new_recipes = str(scoreboard[elf1] + scoreboard[elf2])
    # Add them all to the scoreboard
    scoreboard.extend([int(i) for i in new_recipes])
    # Get the new index
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

# Print it in the format we need
print(''.join([str(i) for i in scoreboard[practice_recipes:practice_recipes+10]]))
