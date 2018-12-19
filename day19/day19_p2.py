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

registers = [1] + [0] * 5
ip = 0
a = 0

for i in range(100):
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

# The program essentially finds the factors of the large number initialised at the start, and adds this to our 0th register
# So find the sum of the factors, and that's what the value will be
# Disclaimer: I got help with this insight
num = registers[2]
ans = 0
for i in range(1, int(num**0.5)+1):
    if num % i == 0:
        ans += i
        ans += num//i
print(ans)