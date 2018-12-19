import inspect
import re
import opcodes

# Load the data
# Process the first line to get the instruction pointer

with open("input.txt", "r") as f:
    data = f.read().splitlines()

instructions = []

for i, line in enumerate(data):
    if i == 0:
        reg_pointer = int(re.findall("\d", line)[0])
    else:
        inst = line.split(" ")
        inst = [inst[0]] + [int(i) for i in inst[1:]]
        instructions.append(inst)

opcode_funcs = inspect.getmembers(opcodes, inspect.isfunction)
# Process these funcs to a dict
instruct_map = {}
for name, opcode in opcode_funcs:
    instruct_map[name] = opcode

registers = [0] * 6
ip = 0
while True:
    # print(ip, instructions[ip])
    # registers[0] = ip
    # Select the instruction
    registers[reg_pointer] = ip

    try:
        curr_inst = instructions[ip]
    # Pointing outside the program
    except IndexError:
        break
    # Run the curr_inst
    registers = instruct_map[curr_inst[0]](registers, curr_inst[1:])

    # Update instruction pointer
    ip = registers[reg_pointer] + 1

    # print(registers)

print(registers[0])