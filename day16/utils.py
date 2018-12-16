from functools import partial

def load_data(fname):
    if "input" in fname:
        with open(fname, "r") as f:
            data_p1, data_p2 = f.read().split("\n\n\n")
        return data_p1, data_p2
    elif "example" in fname:
        with open(fname, "r") as f:
            data = f.read().splitlines()
        return data

def remove_op_code(opcode_map, number):
    # print(opcode_map)
    # print(number)
    for codes in opcode_map.values():
        if number in codes and (len(codes) > 1):
            codes.remove(number)
    return opcode_map