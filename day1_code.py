import utils

fname = utils.load_data(1)
with open(fname,"r") as file:
    vals = file.read().splitlines()
    vals = [int(i) for i in vals]

print(sum(vals))