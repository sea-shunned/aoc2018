import numpy as np
import utils

sleep_array, guard_mapping = utils.process_data()

# Find the guard who slept the most
sleepiest_row = np.argmax(np.sum(sleep_array, axis=1))
# This is annoying, but the dict is small so fine for now
for key, val in guard_mapping.items():
    if val == sleepiest_row:
        sleepiest_guard_id = key
# Find which minute they have slept the most
sleepiest_minute = np.argmax(sleep_array[sleepiest_row], axis=0)
print(sleepiest_guard_id * sleepiest_minute)

# If the data is very large, using a defaultdict with a numpy array might be better
# But if there are many guards a single array is easier to work with