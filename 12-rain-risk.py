filepath = "input/12.txt"

temp = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        temp.append(line.strip())
        line = fp.readline()


def execute(position, direction, instr, part=1):
    action = instr[0]
    value = int(instr[1:])
    if part == 1:
        if action == "N":
            position = (position[0], position[1] + value)
        elif action == "S":
            position = (position[0], position[1] - value)
        elif action == "E":
            position = (position[0] + value, position[1])
        elif action == "W":
            position = (position[0] - value, position[1])
    else:
        if action == "N":
            direction = (direction[0], direction[1] + value)
        elif action == "S":
            direction = (direction[0], direction[1] - value)
        elif action == "E":
            direction = (direction[0] + value, direction[1])
        elif action == "W":
            direction = (direction[0] - value, direction[1])

    if action in ["L", "R"]:
        assert value in [90, 180, 270]
        if value == 180:
            direction = (-direction[0], -direction[1])
        elif (value == 90 and action == "R") or (value == 270 and action == "L"):
            direction = (direction[1], -direction[0])
        elif (value == 90 and action == "L") or (value == 270 and action == "R"):
            direction = (-direction[1], direction[0])
    elif action == "F":
        position = (
            position[0] + value * direction[0],
            position[1] + value * direction[1],
        )
    return position, direction


position = (0, 0)  # (east, north)
direction = (1, 0)

for instr in temp:
    position, direction = execute(position, direction, instr)

print("Part One:", abs(position[0]) + abs(position[1]))

position = (0, 0)  # (east, north)
direction = (10, 1)

for instr in temp:
    position, direction = execute(position, direction, instr, part=2)

print("Part Two:", abs(position[0]) + abs(position[1]))
