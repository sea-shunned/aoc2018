import re
from collections import defaultdict, deque
from itertools import cycle

with open("input.txt", "r") as f:
    data = f.read().split(" ")

num_players, num_marbles = int(data[0]), int(data[-2])

circle = deque([0])
scores = defaultdict(int)
pos = 0
player_cycle = cycle(range(1, num_players+1))

for marble_value in range(1, (num_marbles+1)*100):
    curr_player = next(player_cycle)

    if marble_value % 23 == 0:
        circle.rotate(7)
        scores[curr_player] += marble_value
        scores[curr_player] += circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble_value)

print(max([i for i in scores.values()]))