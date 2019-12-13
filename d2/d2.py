with open("input_p1") as f:
    data = f.read()

data = data.strip()
data = data.split(",")
data = [int(d) for d in data]


def add(data, index):
    print("add")
    data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]


def multiply(data, index):
    print("mul")
    data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]


def op_indexes(data):
    return range(0, len(data), 4)


def op(data, index):
    if data[index] == 1:
        add(data, index)
        return
    if data[index] == 2:
        multiply(data, index)
        return
    if data[index] == 99:
        return True
    raise Exception(f"unknown opcode {data[index]} at index {index} data is {data}")


def run(data, noun, verb):

    data[1] = noun
    data[2] = verb

    print(data)

    for index in op_indexes(data):
        print(data)
        if op(data, index):
            break

    return data[0]


from copy import copy

d2 = copy(data)

print(run(d2, 12, 2))

# start p2

from itertools import product

for noun, verb in product(range(100), range(100)):
    d3 = copy(data)
    if run(d3, noun, verb) == 19690720:
        print(100 * noun + verb)
        break
