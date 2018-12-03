from itertools import cycle

with open("input.txt","r") as file:
    vals = file.read().splitlines()
    vals = [int(i) for i in vals]

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