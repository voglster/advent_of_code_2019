from copy import copy


def process_data(string):
    string = string.strip()
    string = string.split(",")
    return [int(d) for d in string]


class IntComputer:
    def __init__(self):
        self.instruction_pointer = 0
        self.memory = []
        self.indata = None

    def run(self, memory, indata=None):
        self.indata = indata

        self.memory = copy(memory)
        while True:
            opcode = self.opcode()
            if opcode == "99":
                return
            elif opcode == "05":
                self.jump_if_true()
            elif opcode == "06":
                self.jump_if_false()
            elif opcode == "07":
                self.less_than()
            elif opcode == "08":
                self.equals()
            elif opcode == "01":
                self.add()
            elif opcode == "02":
                self.multiply()
            elif opcode == "03":
                self.input()
            elif opcode == "04":
                return self.output()
            else:
                raise Exception(
                    f"Unknown opcode at {self.instruction_pointer}:{opcode}",
                    self.memory[self.instruction_pointer],
                )

    def ref_get(self, index, ref):
        if ref == "1":
            print(f"IMM reading memory at {index} : {self.memory[index]}")
            return self.memory[index]
        print(
            f"reading memory at {self.memory[index]} : {self.memory[self.memory[index]]}"
        )
        return self.memory[self.memory[index]]

    def input(self):
        if self.refs()[1] == "1":
            print(f"get input and save to {self.instruction_pointer + 1}")
        else:
            print(f"get input and save to {self.memory[self.instruction_pointer + 1]}")
        if self.indata is not None:
            v = self.indata
        else:
            v = int(input("Input?"))
        self.set(1, int(v))
        self.instruction_pointer += 2

    def output(self):
        v = self.get(1)
        print(v)
        self.instruction_pointer += 2
        return v

    def get(self, offset):
        return self.ref_get(self.instruction_pointer + offset, self.refs()[offset])

    def set(self, offset, value):
        memloc = self.instruction_pointer + offset
        if self.refs()[offset] == "1":
            print(f"imm saving to {value} to {memloc}")
            self.memory[memloc] = value
        else:
            print(f"saving to {value} to {self.memory[memloc]}")
            self.memory[self.memory[memloc]] = value

    def add(self):
        print("adding")
        v1 = self.get(1)
        v2 = self.get(2)
        print(f"adding {v1} + {v2}")
        self.set(3, v1 + v2)
        self.instruction_pointer += 4

    def multiply(self):
        print("mul")
        v1 = self.get(1)
        v2 = self.get(2)
        self.set(3, v1 * v2)
        self.instruction_pointer += 4

    def less_than(self):
        v1 = self.get(1)
        v2 = self.get(2)
        if v1 < v2:
            self.set(3, 1)
        else:
            self.set(3, 0)
        self.instruction_pointer += 4

    def equals(self):
        v1 = self.get(1)
        v2 = self.get(2)
        if v1 == v2:
            self.set(3, 1)
        else:
            self.set(3, 0)
        self.instruction_pointer += 4

    def jump_if_true(self):
        if self.get(1):
            self.instruction_pointer = self.get(2)
        else:
            self.instruction_pointer += 3

    def jump_if_false(self):
        if not self.get(1):
            self.instruction_pointer = self.get(2)
        else:
            self.instruction_pointer += 3

    def opcode(self):
        opcode = "00000000" + str(self.memory[self.instruction_pointer])
        return opcode[-2:]

    def refs(self):
        opcode = "00000000" + str(self.memory[self.instruction_pointer])
        return "0" + "".join(reversed(opcode[:-2]))


with open("input_p1") as f:
    data = f.read()

# data = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"

problem_data = process_data(data)

comp = IntComputer()

comp.run(problem_data, 5)
