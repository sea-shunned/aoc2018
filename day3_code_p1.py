import utils
import numpy as np

fname = utils.load_data(3)
file = open(fname,"r")
raw_data = file.read().splitlines()
file.close()

data = []
# max_width = 0
# max_height = 0
for line in raw_data:
    line = line.split(" ")
    from_left, from_top = line[2].split(":")[0].split(",")
    from_left, from_top = int(from_left), int(from_top)

    width, height = line[-1].split("x")
    width, height = int(width), int(height)

    # if from_left + width > max_width:
    #     max_width = from_left + width
    # if from_top + height > max_height:
    #     max_height = from_top + height

    data.append((from_left, from_top, width, height))

#sheet = np.zeros((max_height, max_width))

sheet = np.zeros((1000,1000))

for start_col, start_row, width, height in data:
    sheet[start_col:start_col+width, start_row:start_row+height] += 1

print(np.sum(sheet>1))

# Previously had code to identify fabric size as question said "at least 1000" inches
# Turns out it always is