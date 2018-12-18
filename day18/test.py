wrap = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x != 0 or y != 0:
            wrap.append((x, y))

print(wrap)