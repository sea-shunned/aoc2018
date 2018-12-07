import numpy as np
import utils

points, height, width = utils.get_points("input.txt")

grid = utils.calc_grid(points, height, width)

print(np.sum(np.sum(grid, axis=2) < 10000))
