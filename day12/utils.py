def load_data(fname="input.txt"):
    with open(fname, "r") as f:
        data = f.read().splitlines()
    # Get the initial state
    state = data[0].split(" ")[-1]
    # Store the rules
    rules = {}
    # Extract and save the rules
    for line in data[2:]:
        rules[line[:5]] = line[-1]    
    return state, rules

def step(state, rules, ids, buff):
    # Expand the state bit-by-bit
    min_id = ids[0]
    max_id = ids[-1]
    # Add the right id numbers to either side
    ids = list(range(min_id-1, min_id-buff-1, -1))[::-1] + \
          ids + \
          list(range(max_id+1, max_id+buff+1))
    # Create the state for the next step
    new_state = ""
    # Loop over current state
    for i, val in enumerate(state):
        # Get the window for current pot
        window = state[i-2:i+3]
        # If there is no rule for this, just return no plant
        try:
            new_state += rules[window]
        except KeyError:
            new_state += "."
    return new_state, ids
