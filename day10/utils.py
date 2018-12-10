import re

def calc_box_size(xs, ys):
    return (max(xs) - min(xs)) * (max(ys) - min(ys))

def update(xs, ys, vel_xs, vel_ys, direction=1):
    for i, val in enumerate(xs):
        xs[i] += direction * vel_xs[i]
        ys[i] += direction * vel_ys[i]
    return xs, ys

def load_data(fname="input.txt"):
    with open(fname, "r") as f:
        data = f.read().splitlines()

    xs, ys, vel_xs, vel_ys = [], [], [], []

    for line in data:
        x, y, vel_x, vel_y = map(int, re.findall('-?\d+', line))
        xs.append(x)
        ys.append(y)
        vel_xs.append(vel_x)
        vel_ys.append(vel_y) 
    return xs, ys, vel_xs, vel_ys
