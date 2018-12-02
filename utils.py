import os

def load_data(day_num, part_num=None):
	if part_num is None:
		fname = f"day{day_num}_input.txt"
	else:
		fname = f"day{day_num}_input_part{part_num}.txt"
	if os.path.isfile(fname):
		return fname
	else:
		print(fname)
		raise ValueError("Wrong filename specified")