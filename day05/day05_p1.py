import utils

with open("input.txt", "r") as file:
    # Strip the newline off
    raw_data = list(file.read().strip())

print(len(utils.react_polymers(raw_data)))
