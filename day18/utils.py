import copy

def create_area(fname):
    # Read in the data
    with open(fname, "r") as f:
        data = f.read().splitlines()
    end = len(data)
    # Add some buffer around for ease
    area = [[" " for _ in range(end+2)]]
    for line in data:
        area.append(list(" "+line+" "))
    area.append([" " for _ in range(end+2)])
    # Get a list of coords to loop over
    coords = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                coords.append((x, y))
    return area, coords, end

def minute_step(area, coords, end):
    # Create a deepcopy in case
    new_area = copy.deepcopy(area)
    # Loop over the non-buffered area
    for i in range(1, end+1):
        for j in range(1, end+1):
            # Setup the variables
            curr_symbol = area[i][j]
            count_open = 0
            count_trees = 0
            count_lumber = 0
            # Loop over the 8 squares to look at
            for x, y in coords:
                symbol = area[i+y][j+x]
                # Could avoid counting all here but no need
                if symbol == ".":
                    count_open += 1
                elif symbol == "|":
                    count_trees += 1
                elif symbol == "#":
                    count_lumber += 1
            # Check the conditions for change
            if (curr_symbol == ".") and (count_trees >= 3):
                new_area[i][j] = "|"
            if (curr_symbol == "|") and (count_lumber >= 3):
                new_area[i][j] = "#"
            if curr_symbol == "#":
                if not ((count_lumber >= 1) and (count_trees >= 1)):
                    new_area[i][j] = "."
    return new_area

def vis_area(area):
    # Just if we want to look at the state
    for line in area:
        print(''.join(line))

def eval_area(area, end):
    # Evaluate the resource value
    num_woods = 0
    num_lumber = 0
    for i in range(1, end+1):
        for j in range(1, end+1):
            curr_symbol = area[i][j]
            if curr_symbol == "#":
                num_lumber += 1
            elif curr_symbol == "|":
                num_woods += 1
    return num_lumber * num_woods
    