def addr(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] + registers[instruction[1]]
    return registers

def addi(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] + instruction[1]
    return registers

def mulr(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] * registers[instruction[1]]
    return registers

def muli(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] * instruction[1]
    return registers

def banr(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] & registers[instruction[1]]
    return registers

def bani(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] & instruction[1]
    return registers

def borr(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] | registers[instruction[1]]
    return registers

def bori(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]] | instruction[1]
    return registers

def setr(registers, instruction):
    registers[instruction[2]] = registers[instruction[0]]
    return registers

def seti(registers, instruction):
    registers[instruction[2]] = instruction[0]
    return registers

def gtir(registers, instruction):
    if instruction[0] > registers[instruction[1]]:
        registers[instruction[2]] = 1
    else:
        registers[instruction[2]] = 0
    return registers

def gtri(registers, instruction):
    if registers[instruction[0]] > instruction[1]:
        registers[instruction[2]] = 1
    else:
        registers[instruction[2]] = 0
    return registers

def gtrr(registers, instruction):
    if registers[instruction[0]] > registers[instruction[1]]:
        registers[instruction[2]] = 1
    else:
        registers[instruction[2]] = 0
    return registers

def eqir(registers, instruction):
    if instruction[0] == registers[instruction[1]]:
        registers[instruction[2]] = 1
    else:
        registers[instruction[2]] = 0
    return registers

def eqri(registers, instruction):
    if registers[instruction[0]] == instruction[1]:
        registers[instruction[2]] = 1
    else:
        registers[instruction[2]] = 0
    return registers

def eqrr(registers, instruction):
    if registers[instruction[0]] == registers[instruction[1]]:
        registers[instruction[2]] = 1
    else:
        registers[instruction[2]] = 0
    return registers
