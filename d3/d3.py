with open("input_p1") as f:
    data = f.readlines()

data = [d.strip() for d in data]


def convert_to_coord_pairs(line):
    current_pos = (0, 0)
    for command in line.split(","):
        command_letter = command[0]
        count = int(command[1:])
        if command_letter == "R":
            new_pos = (current_pos[0] + count, current_pos[1])
        elif command_letter == "L":
            new_pos = (current_pos[0] - count, current_pos[1])
        elif command_letter == "U":
            new_pos = (current_pos[0], current_pos[1] + count)
        elif command_letter == "D":
            new_pos = (current_pos[0], current_pos[1] - count)
        else:
            raise Exception(f"unknown dir {command_letter}")
        yield current_pos, new_pos
        current_pos = new_pos


def find_cross(pair1, pair2):
    (x0, y0), (x1, y1) = pair1
    pair1_vertical = x0 == x1
    (x2, y2), (x3, y3) = pair2
    pair2_vertical = x2 == x3
    if pair1_vertical == pair2_vertical:
        return False
    if pair1_vertical:
        ylow, yhigh = sorted((y0, y1))
        xlow, xhigh = sorted((x2, x3))
        if ylow <= y2 <= yhigh and xlow <= x0 <= xhigh:
            # must intersect
            return x0, y2
    ylow, yhigh = sorted((y2, y3))
    xlow, xhigh = sorted((x0, x1))
    if ylow <= y0 <= yhigh and xlow <= x2 <= xhigh:
        # must intersect
        return x2, y0
    return False


pairs1 = list(convert_to_coord_pairs(data[0]))
pairs2 = list(convert_to_coord_pairs(data[1]))

from itertools import product

min_dist = 100000000000

for line1, line2 in product(pairs1, pairs2):
    x = find_cross(line1, line2)
    if x:
        new_dist = abs(x[0]) + abs(x[1])
        min_dist = min(new_dist, min_dist)

print(min_dist)
