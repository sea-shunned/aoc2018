with open("input.txt","r") as file:
    vals = file.read().splitlines()
    vals = [int(i) for i in vals]

print(sum(vals))