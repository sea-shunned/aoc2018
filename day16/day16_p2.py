import inspect
import re
from collections import defaultdict
import utils
import opcodes

# Get data
data, data_p2 = utils.load_data("input.txt")
data = data.split("\n\n")
# Initialise variables
opcode_funcs = inspect.getmembers(opcodes, inspect.isfunction)
opcode_map = defaultdict(set)
# Loop over input
for example in data:
    # Get the relevant 3 lines
    before, instruction, after = example.splitlines()
    # Get the numbers
    registers = [int(i) for i  in re.findall('\d+', before)]
    instruction = [int(i) for i  in re.findall('\d+', instruction)]
    expected_res = [int(i) for i  in re.findall('\d+', after)]
    # See if it's a match
    for name, opcode in opcode_funcs:
        reg = registers.copy()
        res = opcode(reg, instruction[1:])
        if res == expected_res:
            # Add as a candidate
            opcode_map[name].add(instruction[0])

# Use a process of elimination to get the unique op code
seen = set()
while True:
    for key, val in opcode_map.items():
        if (len(val) == 1):
            number, = val
            if number not in seen:
                seen.add(number)
                opcode_map = utils.remove_op_code(opcode_map, number)
                break
    else:
        break

# Construct the instruction number to opcode function mapping
instruct_map = {}
for name, opcode in opcode_funcs:
    number, = opcode_map[name]
    instruct_map[number] = opcode

# Initial empty register
reg = [0,0,0,0]
# Loop over the instructions (skip first empty line)
for instruction in data_p2.splitlines()[1:]:
    instruction = [int(i) for i  in re.findall('\d+', instruction)]
    # Call the appropriate opcode
    reg = instruct_map[instruction[0]](reg, instruction[1:])

print(reg[0])