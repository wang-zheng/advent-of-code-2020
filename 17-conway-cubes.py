from collections import defaultdict

filepath = "input/17.txt"


def neighbors_3d(point):
    list_ = []
    for x in range(point[0] - 1, point[0] + 2):
        for y in range(point[1] - 1, point[1] + 2):
            for z in range(point[2] - 1, point[2] + 2):
                list_.append((x, y, z))
    list_.remove(point)
    return list_


space = defaultdict(lambda: False)
map_ = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        map_.append(line.strip())
        line = fp.readline()

for y, line in enumerate(map_):
    for x, char in enumerate(line):
        if char == "#":
            space[(x, y, 0)] = True

space_copy = space.copy()


def cycle(space, neighbors):
    new = space.copy()
    groups = [neighbors(point) for point in space.keys() if space[point]]
    unique = []
    unique = [point for group in groups for point in group if point not in unique]
    [
        unique.append(point)
        for point in space.keys()
        if space[point] and point not in unique
    ]
    for point in unique:
        active = len([0 for near in neighbors(point) if space[near]])
        if space[point] and (active < 2 or active > 3):
            new[point] = False
        elif not space[point] and active == 3:
            new[point] = True
    return new


def pretty_print(space, step=1):
    start = 0 - step
    end = 3 + step
    for z in range(start, end - 2):
        print("z = ", z)
        for y in range(start, end):
            line = ""
            for x in range(start, end):
                line += "#" if space[(x, y, z)] else "."
            print(line)
        print("")


for i in range(6):
    # if i <= 3:
    #    pretty_print(space,i)
    space = cycle(space, neighbors_3d)

total = list(space.values()).count(True)
print("Part One:", total)

space = defaultdict(lambda: False)
for key, val in space_copy.items():
    space[(key[0], key[1], key[2], 0)] = val


def neighbors_4d(point):
    list_ = []
    for x in range(point[0] - 1, point[0] + 2):
        for y in range(point[1] - 1, point[1] + 2):
            for z in range(point[2] - 1, point[2] + 2):
                for w in range(point[3] - 1, point[3] + 2):
                    list_.append((x, y, z, w))
    list_.remove(point)
    return list_


for i in range(6):
    space = cycle(space, neighbors_4d)

total = list(space.values()).count(True)
print("Part Two:", total)
