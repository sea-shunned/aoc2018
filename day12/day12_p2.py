from collections import defaultdict
import utils

state, rules = utils.load_data()

ids = [i for i in range(len(state))]

buff = 500

def run_gens(num_gens, state, rules, ids, buff):
    # Keep track of the previous score and differences
    # To identify if we reach steady-state
    diffs = defaultdict(int)
    prev_score = 0
    
    # Loop over the generations
    for gen in range(num_gens):	
        # Add the empty pots either side
        state = "."*buff + state + "."*buff
        # Take a step
        state, ids = utils.step(state, rules, ids, buff)
        # Add up the id numbers of the pots with plants
        sum_pots = 0
        for id_num, value in zip(ids, state):
            if value == "#":
                sum_pots += id_num
        # Calculate the difference and count it
        diff = sum_pots - prev_score
        prev_score = sum_pots
        diffs[diff] += 1
        # If we have counted enough of the same difference, break!
        if diffs[diff] == 10:
            break
    return state, ids, gen, diff

state, ids, gen, diff = run_gens(2000, state, rules, ids, buff)

sum_pots = 0
for id_num, value in zip(ids, state):
    if value == "#":
        sum_pots += id_num

print(sum_pots + ((50000000000-(gen+1))*diff))