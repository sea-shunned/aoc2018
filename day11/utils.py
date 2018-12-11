import numpy as np

def calc_power(serial_num):
    grid = np.repeat(
    np.arange(1, 301, 1, dtype=int)[:, np.newaxis],
    300,
    axis=1)

    grid += 10
    rack_id = grid.copy()
    grid *= np.arange(1, 301, 1, dtype=int)[np.newaxis, :]
    grid += serial_num
    grid = np.multiply(grid, rack_id)
    grid = np.divide(grid, 100).astype(int)
    grid = np.remainder(grid, 10)
    grid -= 5

    return grid