import numpy as np

with open("input.txt","r") as file:
    raw_data = file.read().splitlines()

data = []
for line in raw_data:
    line = line.split(" ")
    claim_id = int(line[0][1:])
    from_left, from_top = line[2].split(":")[0].split(",")
    from_left, from_top = int(from_left), int(from_top)

    width, height = line[-1].split("x")
    width, height = int(width), int(height)

    data.append((claim_id, from_left, from_top, width, height))

sheet = np.zeros((1000,1000))

for claim_id, y, x, width, height in data:
    sheet[y:y+width, x:x+height] += 1

# Need to loop a second time because of order of data
for claim_id, y, x, width, height in data:
    if np.all(sheet[y:y+width, x:x+height] == 1):
        print(claim_id)
