import utils
from collections import defaultdict

fname = utils.load_data(2)
file = open(fname,"r")
data = file.read().splitlines()
file.close()

for i, id_num in enumerate(data):
	for other_id in data[i:]:
		counter = 0
		for j, letter in enumerate(id_num):
			if letter != other_id[j]:
				counter += 1
			if counter == 2:
				break
		if counter == 1:
			res = [id_num, other_id]

ans = []

for i, letter in enumerate(res[0]):
	if letter == res[1][i]:
		ans.append(letter)

print("".join(ans))