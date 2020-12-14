import re
from itertools import product

filepath = "input/14.txt"


def parse(line):
    parts = re.split("\W+", line)
    parts = [part for part in parts if part != ""]
    return parts


def apply_1(mask, num):
    str = format(num, "#038b")
    for i, bit in enumerate(mask):
        if bit != "X":
            str = str[: i + 2] + bit + str[i + 3 :]
    return int(str, 2)


commands = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        commands.append(parse(line))
        line = fp.readline()

mask = None
mem = {}
for command in commands:
    if command[0] == "mask":
        mask = command[1]
    elif command[0] == "mem":
        index = int(command[1])
        value = apply_1(mask, int(command[2]))
        mem[index] = value

print("Part One:", sum(mem.values()))


def apply_2(mask, num):
    str = format(num, "#038b")[2:]
    for i, bit in enumerate(mask):
        if bit != "0":
            str = str[:i] + bit + str[i + 1 :]
    return str


def put_in(mem, index, value):
    xs = [i for i, bit in enumerate(index) if bit == "X"]
    if len(xs) == 0:
        mem[int(index, 2)] = value
        return None
    for bits in product("01", repeat=len(xs)):
        new_index = index
        for i, j in enumerate(xs):
            new_index = new_index[:j] + bits[i] + new_index[j + 1 :]
        mem[int(new_index, 2)] = value
    return None


mem = {}
for command in commands:
    if command[0] == "mask":
        mask = command[1]
    elif command[0] == "mem":
        index = apply_2(mask, int(command[1]))
        value = int(command[2])
        put_in(mem, index, value)

print("Part Two:", sum([x for x in mem.values()]))
