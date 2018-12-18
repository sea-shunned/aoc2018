from collections import defaultdict
import utils
# Get the initial area
area, coords, end = utils.create_area("input.txt")
# Setup a scores dict
scores = defaultdict(int)
# Do some initial loops to get the repeating sequence
for minute in range(1, 1001):
    area = utils.minute_step(area, coords, end)
    resource_val = utils.eval_area(area, end)
    scores[resource_val] += 1
# Identify the length of this period/sequence
seq_length = 0
for score, count in scores.items():
    if count > 10:
        seq_length += 1
# Loop until we get the right value
for minute in range(1001,5000):
    area = utils.minute_step(area, coords, end)
    resource_val = utils.eval_area(area, end)
    utils.vis_area(area)
    # Find what the value will be during the period on the 1000000000th minute
#     if (1000000000 - minute) % 28 == 0:
#         print(resource_val)
#         break
