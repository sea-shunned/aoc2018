import inspect
import re
import utils
import opcodes

# Get data
data, _ = utils.load_data("input.txt")
data = data.split("\n\n")
# Initialise variables
opcode_funcs = inspect.getmembers(opcodes, inspect.isfunction)
ans = 0
# Loop over input
for example in data:
    # Get the relevant 3 lines
    before, instruction, after = example.splitlines()
    # Get the numbers
    registers = [int(i) for i  in re.findall('\d+', before)]
    instruction = [int(i) for i  in re.findall('\d+', instruction)]
    expected_res = [int(i) for i  in re.findall('\d+', after)]
    # See if it's a match
    count = 0
    for name, opcode in opcode_funcs:
        reg = registers.copy()
        res = opcode(reg, instruction[1:])
        if res == expected_res:
            count += 1
    if count >= 3:
        ans += 1

print(ans)