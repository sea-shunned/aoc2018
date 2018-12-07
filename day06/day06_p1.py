import numpy as np
import utils

points, height, width = utils.get_points("input.txt")

grid = utils.calc_grid(points, height, width)

closest_1 = np.argsort(grid, axis=2)[:, :, 0]
closest_2 = len(points) - 1 - np.argsort(grid[:, :, ::-1], axis=2)[:, :, 0]
inf_grid = np.where(closest_1 == closest_2, closest_1, len(points))

edges = np.unique(
    np.concatenate((
        inf_grid[0, :],
        inf_grid[-1, :],
        inf_grid[:, 0],
        inf_grid[:, -1]))
)

_, counts = np.unique(inf_grid, return_counts=True)
print(np.max(np.delete(counts, edges)))
