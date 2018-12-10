import utils
import matplotlib.pyplot as plt

xs, ys, vel_xs, vel_ys = utils.load_data()

box_size = 10000000000000

while True:
    xs, ys = utils.update(xs, ys, vel_xs, vel_ys)
    new_size = utils.calc_box_size(xs, ys)
    if box_size < new_size:
        break
    else:
        box_size = new_size

xs, ys = utils.update(xs, ys, vel_xs, vel_ys, direction=-1)

fig, ax = plt.subplots()
ax.scatter(xs, [-i for i in ys])
plt.axis('equal')
plt.show()