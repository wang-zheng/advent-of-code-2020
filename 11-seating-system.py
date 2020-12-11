filepath = "input/11.txt"

temp = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        temp.append("." + line.strip() + ".")
        line = fp.readline()

# pad the surroundings with "." to make it easier to check neighbors
col = len(temp[0])
temp.append("." * col)
seats = ["." * col]
seats.extend(temp)
row = len(seats)


def iter_1(seats):
    new_seats = seats.copy()
    changed = False
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            neighbors = (
                seats[i - 1][j - 1 : j + 2]
                + seats[i][j - 1]
                + seats[i][j + 1]
                + seats[i + 1][j - 1 : j + 2]
            )
            occupied = neighbors.count("#")
            if occupied == 0 and seats[i][j] == "L":
                changed = True
                new_seats[i] = new_seats[i][:j] + "#" + new_seats[i][j + 1 :]
            elif occupied >= 4 and seats[i][j] == "#":
                changed = True
                new_seats[i] = new_seats[i][:j] + "L" + new_seats[i][j + 1 :]
    return new_seats, changed


seats_copy = seats.copy()
changed = True
while changed:
    seats, changed = iter_1(seats)

# print("\n".join(seats))
print("Part One:", "\n".join(seats).count("#"))

seats = seats_copy.copy()
row = len(seats)
col = len(seats[0])

# dictionary of neighbors to each seat
graph = {(i, j): [] for i in range(row) for j in range(col)}

for i in range(row):
    j_list = [j for j in range(col) if seats[i][j] == "L"]
    [graph[(i, j_1)].append((i, j_2)) for (j_1, j_2) in zip(j_list[:-1], j_list[1:])]
    [graph[(i, j_2)].append((i, j_1)) for (j_1, j_2) in zip(j_list[:-1], j_list[1:])]

for j in range(col):
    i_list = [i for i in range(row) if seats[i][j] == "L"]
    [graph[(i_1, j)].append((i_2, j)) for (i_1, i_2) in zip(i_list[:-1], i_list[1:])]
    [graph[(i_2, j)].append((i_1, j)) for (i_1, i_2) in zip(i_list[:-1], i_list[1:])]

for d in range(-row + 1, col):
    pos_list = [
        (x, d + x)
        for x in range(row)
        if (d + x) in range(col) and seats[x][d + x] == "L"
    ]
    [graph[pos_1].append(pos_2) for (pos_1, pos_2) in zip(pos_list[:-1], pos_list[1:])]
    [graph[pos_2].append(pos_1) for (pos_1, pos_2) in zip(pos_list[:-1], pos_list[1:])]

for d in range(col + row):
    pos_list = [
        (x, d - x)
        for x in range(row)
        if (d - x) in range(col) and seats[x][d - x] == "L"
    ]
    [graph[pos_1].append(pos_2) for (pos_1, pos_2) in zip(pos_list[:-1], pos_list[1:])]
    [graph[pos_2].append(pos_1) for (pos_1, pos_2) in zip(pos_list[:-1], pos_list[1:])]


def iter_2(seats):
    new_seats = seats.copy()
    changed = False
    for pos in graph.keys():
        i = pos[0]
        j = pos[1]
        sight = "".join([seats[node[0]][node[1]] for node in graph[pos]])
        occupied = sight.count("#")
        if occupied == 0 and seats[i][j] == "L":
            changed = True
            new_seats[i] = new_seats[i][:j] + "#" + new_seats[i][j + 1 :]
        elif occupied >= 5 and seats[i][j] == "#":
            changed = True
            new_seats[i] = new_seats[i][:j] + "L" + new_seats[i][j + 1 :]
    return new_seats, changed


changed = True
while changed:
    seats, changed = iter_2(seats)

# print("\n".join(seats))
print("Part Two:", "\n".join(seats).count("#"))
