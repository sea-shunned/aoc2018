import utils
from itertools import cycle

fname = utils.load_data(1)
file = open(fname,"r")
vals = [int(i) for i in file.read().splitlines()]
file.close()

freq = 0
seen_freqs = set()
seen_freqs.add(freq)

for val in cycle(vals):
    freq += val
    if freq in seen_freqs:
        print(freq)
        break
    else:
        seen_freqs.add(freq)