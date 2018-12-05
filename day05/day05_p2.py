import utils

with open("input.txt", "r") as file:
    # Strip the newline off
    raw_data = file.read().strip()

## We can apply part 1 first to shorten the input
# Roughly 5x speed-up
# raw_data = utils.react_polymers(raw_data)

# Only look at the letters that exist
uniq_letters = set([i.lower() for i in raw_data])
# Dict to store results
results = {}
# Run part 1 for each letter
for uniq_letter in uniq_letters:
    seq = raw_data.replace(uniq_letter, "").replace(uniq_letter.upper(), "")
    results[uniq_letter] = len(utils.react_polymers(seq))

# Print the relevant key and polymer length
print(sorted(results.items(), key=lambda kv: kv[1])[0])
