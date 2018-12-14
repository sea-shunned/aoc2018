# Turn into a list of ints for comparing
practice_recipes = [int(i) for i in '793031']
# Avoid repeated len calls
window_size = len(practice_recipes)
# Initial recipe scores
scoreboard = [3, 7]
# Indices for the elves current position
elf1 = 0
elf2 = 1
# Flag for while loop
unfound = True
# Keep searching until it's found
while unfound:
    # Turn into string to get each digit
    new_recipes = str(scoreboard[elf1] + scoreboard[elf2])
    # Add each digit individually in case the answer is after only 1 of the digits
    for score in new_recipes:
        scoreboard.append(int(score))
        # Need to break the while loop
        if scoreboard[-window_size:] == practice_recipes:
            unfound = False
            break
    # Get the new index
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

print(len(scoreboard[:-window_size]))
