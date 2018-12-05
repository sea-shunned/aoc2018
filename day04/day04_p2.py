import numpy as np
import utils

sleep_array, guard_mapping = utils.process_data()

# Find the guard who has slept the most on a particular minute
sleepiest_row = np.argmax(np.max(sleep_array, axis=1))
# This is annoying, but the dict is small so fine for now
for key, val in guard_mapping.items():
    if val == sleepiest_row:
        sleepiest_guard_id = key
# Find which minute they have slept the most
sleepiest_minute = np.argmax(sleep_array[sleepiest_row])
print(sleepiest_guard_id * sleepiest_minute)