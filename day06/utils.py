from collections import namedtuple
import numpy as np

def get_points(fname):
    with open(fname, "r") as file:
        data = file.read().splitlines()

    Point = namedtuple("Point", ['x', 'y'])

    points = []

    min_x = np.inf
    max_x = 0
    min_y = np.inf
    max_y = 0

    for line in data:
        x, y = map(int, line.split(", "))

        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        points.append(Point(x, y))

    height = max_y-min_y + int(0.5*(max_y-min_y))
    width = max_x-min_x + int(0.5*(max_x-min_x))
    
    return points, height, width

def calc_grid(points, height, width):
    x_coords, y_coords = np.meshgrid(np.arange(width), np.arange(height))

    grid = np.zeros((height, width, len(points)))

    for i, point in enumerate(points):
        grid[:, :, i] = np.abs(point.x - x_coords) + np.abs(point.y - y_coords)

    return grid