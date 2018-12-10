import utils

xs, ys, vel_xs, vel_ys = utils.load_data()
box_size = 10000000000000
a = 0

while True:
    xs, ys = utils.update(xs, ys, vel_xs, vel_ys)
    new_size = utils.calc_box_size(xs, ys)
    if box_size < new_size:
        break
    else:
        box_size = new_size
    a += 1

print(a)