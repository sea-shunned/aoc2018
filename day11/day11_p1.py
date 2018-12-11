import numpy as np
import utils

grid = utils.calc_power(5468)

best_sum = 0

for i in range(296):
    for j in range(296):
        curr_sum = np.sum(grid[i:i+3, j:j+3])

        if curr_sum > best_sum:
            best_sum = curr_sum
            top_left_coord = (i+1, j+1)

print(top_left_coord)