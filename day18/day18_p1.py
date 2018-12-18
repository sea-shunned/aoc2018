import utils
# Get the initial area
area, coords, end = utils.create_area("input.txt")
# Loop for the first 10 minutes
for minute in range(10):
    area = utils.minute_step(area, coords, end)
# utils.vis_area(area)
print(utils.eval_area(area, end))
