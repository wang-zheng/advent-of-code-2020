from collections import defaultdict

filepath = "input/24.txt"


def parse(line):
    i = 0
    e = 0
    ne = 0
    while i < len(line):
        if line[i] == "w":
            e -= 1
        elif line[i] == "e":
            e += 1
        elif line[i : i + 2] == "ne":
            ne += 1
        elif line[i : i + 2] == "nw":
            ne += 1
            e -= 1
        elif line[i : i + 2] == "se":
            ne -= 1
            e += 1
        elif line[i : i + 2] == "sw":
            ne -= 1

        if line[i] in ["n", "s"]:
            i += 1
        i += 1

    return (e, ne)


flipped = defaultdict(bool)
with open(filepath) as fp:
    line = fp.readline()
    while line:
        coord = parse(line.strip())
        flipped[coord] = not flipped[coord]
        line = fp.readline()


ans = list(flipped.values()).count(True)

print("Part One:", ans)


def neighbors(coord):
    (e, ne) = coord
    return [
        (e + 1, ne),
        (e - 1, ne),
        (e, ne + 1),
        (e, ne - 1),
        (e - 1, ne + 1),
        (e + 1, ne - 1),
    ]


check = [coord for point in flipped.keys() for coord in neighbors(point)]
check = set(check + list(flipped.keys()))

for day in range(100):
    flip = []
    for point in check:
        count = [flipped[x] for x in neighbors(point)].count(True)
        if flipped[point] and (count == 0 or count > 2):
            flip.append(point)
        elif not flipped[point] and count == 2:
            flip.append(point)

    for point in flip:
        flipped[point] = not flipped[point]

    [check.add(x) for point in flip for x in neighbors(point) if flipped[point]]
ans = list(flipped.values()).count(True)
print("Part Two:", ans)
