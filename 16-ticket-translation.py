import re

filepath = "input/16.txt"


def parse_field(line):
    text = [part.strip() for part in re.split(":| or |-", line)]
    return (text[0], int(text[1]), int(text[2]), int(text[3]), int(text[4]))


# parse input into fields, your ticket and nearby tickets
fields = []
nearby = []
with open(filepath) as fp:
    line = fp.readline()
    while line.strip() != "":
        fields.append(parse_field(line))
        line = fp.readline()

    line = fp.readline()
    assert line.strip() == "your ticket:"
    line = fp.readline()
    you = [int(x) for x in line.split(",")]

    line = fp.readline()
    line = fp.readline()
    assert line.strip() == "nearby tickets:"
    line = fp.readline()
    while line:
        nearby.append([int(x) for x in line.split(",")])
        line = fp.readline()


def check(field, num):
    return (field[1] <= num <= field[2]) or (field[3] <= num <= field[4])


# find invalid tickets
total = 0
invalid = []
for i, ticket in enumerate(nearby):
    for num in ticket:
        valid = False
        for field in fields:
            if check(field, num):
                valid = True
        if not valid:
            invalid.append(i)
            total += num

print("Part One:", total)

# remove invalid tickets
nearby = [ticket for i, ticket in enumerate(nearby) if i not in invalid]

# find all valid positions for a field
position = {i: [] for i in range(len(fields))}
for i, field in enumerate(fields):
    for j in range(len(nearby[0])):
        valid = True
        for ticket in nearby:
            if not check(field, ticket[j]):
                valid = False
                break
        if valid:
            position[i].append(j)


def finish(position):
    uncertainty = [len(x) for x in position.values()]
    return all([x == 1 for x in uncertainty[:6]])


# repeatedly eliminate positions that are taken by other fields
checked = []
while not finish(position):
    new = [i for i, arr in position.items() if len(arr) == 1 and i not in checked]
    for i, arr in position.items():
        for index in new:
            if i != index and position[index][0] in arr:
                position[i].remove(position[index][0])
    checked.extend(new)

ans = 1
for i in range(6):
    ans *= you[position[i][0]]
print("Part Two:", ans)
