import utils

state, rules = utils.load_data()

# Create initial id numbers for the pots
ids = [i for i in range(len(state))]

# A buffer for either side
buff = 10

def run_gens(num_gens, state, rules, ids, buff):
    # Loop over the generations
    for gen in range(num_gens):
        # Add the empty pots either side
        state = "."*buff + state + "."*buff
        # Take a step
        state, ids = utils.step(state, rules, ids, buff)
    return state, ids

state, ids = run_gens(20, state, rules, ids, buff)

# Add up the id numbers of the pots with plants
sum_pots = 0
for id_num, value in zip(ids, state):
    if value == "#":
        sum_pots += id_num

print(sum_pots)