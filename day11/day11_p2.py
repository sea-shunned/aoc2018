import numpy as np
import utils

grid = utils.calc_power(5468)

summed_area = np.cumsum(np.cumsum(grid, axis=0), axis=1)
best_sum = 0
best_size = 0

for s in range(2, 300):
    for i in range(299-s):
        for j in range(299-s):
            curr_sum = summed_area[i, j] \
                       + summed_area[i+s, j+s] \
                       - summed_area[i+s, j] \
                       - summed_area[i, j+s] \

            if curr_sum > best_sum:
                best_size = s
                best_sum = curr_sum
                top_left_coord = (i+1,j+1)
                
print(best_size, best_sum, top_left_coord)