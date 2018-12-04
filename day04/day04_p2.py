import numpy as np
from datetime import datetime

with open("input.txt", "r") as file:
    raw_data = file.read().splitlines()

# Sort the data by the time
# As the data follows the same format, this is overkill
# A simple (lexicographic) sort would suffice
raw_data = sorted(raw_data, key=
    lambda x:datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'))

# Find the unique guard ids
guard_ids = set()
for line in raw_data:
    text = line[19:]
    if text[0] == "G":
        guard_ids.add(int(text.split(" ")[1].split("#")[-1]))

# Create a mapping for the row number and id number
guard_mapping = {}
for i, id_num in enumerate(guard_ids):
    guard_mapping[id_num] = i

# Create an array for all sleep time to work with
sleep_array = np.zeros((len(guard_ids), 60))

# Count each time they have slept for a particular minute
for line in raw_data:
    text = line[19:]
    if text[0] == "G":
        current_guard = int(text.split(" ")[1].split("#")[-1])
    elif text[0] == "f":
        sleep_start = int(line[15:17])
    elif text[0] == "w":
        sleep_end = int(line[15:17])
        sleep_array[guard_mapping[current_guard], sleep_start:sleep_end] += 1

# Find the guard who has slept the most on a particular minute
sleepiest_row = np.argmax(np.max(sleep_array, axis=1))
# This is annoying, but the dict is small so fine for now
for key, val in guard_mapping.items():
    if val == sleepiest_row:
        sleepiest_guard_id = key
# Find which minute they have slept the most
sleepiest_minute = np.argmax(sleep_array[sleepiest_row])
print(sleepiest_guard_id * sleepiest_minute)