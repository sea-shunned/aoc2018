from collections import defaultdict

with open("input.txt","r") as file:
    data = file.read().splitlines()

two_letters = 0
three_letters = 0

for id_num in data:
    letter_counts = defaultdict(int)
    
    for letter in id_num:
        letter_counts[letter] += 1

    if 2 in letter_counts.values():
        two_letters += 1
    if 3 in letter_counts.values():
        three_letters += 1

print(two_letters*three_letters)

# When we have counted two letters and three letters once, we could break from that id number
# Unless the input scales though this is unnecessary