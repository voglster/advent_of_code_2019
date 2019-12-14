with open("input_p1") as f:
    data = f.read()

data = data.strip()
data = data.split(",")
data = [int(d) for d in data]


def input_func(data, index, ref):
    if ref == "1":
        data[index + 1] = int(input())
    else:
        data[data[index + 1]] = int(input())


def output_func(data, index, ref):
    if ref == "1":
        print(data[index + 1])
    else:
        print(data[data[index + 1]])


def add(data, index, ref):
    if ref[0] == "1":
        p1 = data[index + 1]
    else:
        p1 = data[data[index + 1]]

    if ref[1] == "1":
        p2 = data[index + 2]
    else:
        p2 = data[data[index + 2]]
    assert ref[2] == "0"
    data[data[index + 3]] = p1 + p2


def multiply(data, index, ref):
    if ref[0] == "1":
        p1 = data[index + 1]
    else:
        p1 = data[data[index + 1]]

    if ref[1] == "1":
        p2 = data[index + 2]
    else:
        p2 = data[data[index + 2]]
    assert ref[2] == "0"
    data[data[index + 3]] = p1 * p2


def break_func(data, index, ref):
    import sys

    sys.exit(0)


operations = {
    "01": (add, 4),
    "02": (multiply, 4),
    "03": (input_func, 2),
    "04": (output_func, 2),
    "99": (break_func, 1),
}


def interpet_operation(opcode):
    opcode = "00000000" + str(opcode)
    last_two = opcode[-2:]
    operation, index_offset = operations[last_two]
    ref = "".join(reversed(opcode[:-2]))
    ref = ref[: index_offset - 1]
    return operation, index_offset, ref


current_index = 0
while True:
    operation, index_offset, ref = interpet_operation(data[current_index])
    operation(data, current_index, ref)
    current_index += index_offset
