from math import prod, sqrt

filepath = "input/20.txt"


tiles = []
tile = []
ids = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        if line[:4] == "Tile":
            ids.append(int(line[5:9].strip()))
        elif line.strip() == "":
            tiles.append(tile.copy())
            tile = []
        else:
            tile.append(line.strip())
        line = fp.readline()

if tile:
    tiles.append(tile)

assert len(tiles) == len(ids)


def edges(tile):
    top = tile[0]
    right = "".join([row[-1] for row in tile])
    bottom = tile[-1][::-1]
    left = "".join([row[0] for row in tile[::-1]])
    return [top, right, bottom, left].copy()


matches = []


def match(edges_1, edges_2):
    for edge_1 in edges_1:
        for edge_2 in edges_2:
            if edge_1 == edge_2[::-1] or edge_1 == edge_2:
                return True
    return False


all_edges = []
for tile in tiles:
    all_edges.append(edges(tile))

scores = []
for i in range(len(tiles)):
    this = all_edges[i]
    others = all_edges[:i] + all_edges[i + 1 :]
    score = 0
    for other in others:
        if match(this, other):
            score += 1
    scores.append(score)

corners = [ids[i] for i in range(len(tiles)) if scores[i] == 2]
assert len(corners) == 4
print("Part One:", prod(corners))


def flip(tile):
    new_tile = []
    for i in range(len(tile)):
        new_tile.append(tile[i][::-1])
    return new_tile


def rotate(tile):
    new_tile = []
    for i in range(len(tile[0])):
        new_tile.append("".join([row[i] for row in tile[::-1]]))
    return new_tile


def pretty_print(tiles):
    for i in range(len(tiles[0])):
        [print(tile[i], end=" ") for tile in tiles]
        print("")
    print("")


def find_match(tile_ind, side_ind):
    edge = all_edges[tile_ind][side_ind]
    for i in range(len(all_edges)):
        if i == tile_ind:
            continue
        for j, test in enumerate(all_edges[i]):
            if edge == test[::-1]:
                return i, j, True  # tile index, side index, matching
            elif edge == test:
                return i, j, False
    return -1, -1, False


def global_flip(ind):
    tiles[ind] = flip(tiles[ind])
    all_edges[ind] = edges(tiles[ind])


def global_rotate(ind):
    tiles[ind] = rotate(tiles[ind])
    all_edges[ind] = edges(tiles[ind])


# some enums
TOP = 0
RIGHT = 1
BOT = 2
LEFT = 3

n = int(sqrt(len(tiles)))


assembled = [[-1] * n for _ in range(n)]

# top left corner
tile_ind = [i for i in range(len(tiles)) if scores[i] == 2][0]
assembled[0][0] = tile_ind
global_flip(tile_ind)
sides = []
for side_ind in range(4):
    new_tile_ind, _, _ = find_match(tile_ind, side_ind)
    if new_tile_ind != -1:
        sides.append(side_ind)

side_ind = [ind for ind in sides if (ind + 1) % 4 in sides][0]
num_rotations = (RIGHT - side_ind) % 4
for _ in range(num_rotations):
    global_rotate(tile_ind)

# assemble the first row based on tile on the left
for j in range(1, n):
    tile_ind, side_ind, match = find_match(assembled[0][j - 1], RIGHT)
    assembled[0][j] = tile_ind
    num_rotations = (LEFT - side_ind) % 4 if match else (RIGHT - side_ind) % 4

    for _ in range(num_rotations):
        global_rotate(tile_ind)

    if not match:
        global_flip(tile_ind)

# assemble all other rows based on tile above
for i in range(1, n):
    for j in range(0, n):
        tile_ind, side_ind, match = find_match(assembled[i - 1][j], BOT)
        assembled[i][j] = tile_ind
        num_rotations = (TOP - side_ind) % 4

        for _ in range(num_rotations):
            global_rotate(tile_ind)

        if not match:
            global_flip(tile_ind)

# print the tiles
# for i in range(n):
#    pretty_print([tiles[ind] for ind in assembled[i]])


def inner(tile):
    new_tile = []
    for i in range(1, len(tile) - 1):
        new_tile.append(tile[i][1:-1])
    return new_tile


image = []
for i in range(n):
    parts = [inner(tiles[ind]) for ind in assembled[i]]
    for row in range(len(parts[0])):
        image.append("".join([part[row] for part in parts]))

# pretty_print([image])

monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

hgt = len(monster)
wdt = len(monster[0])


def spotted(ind_i, ind_j, image):
    for i in range(hgt):
        for j in range(wdt):
            if monster[i][j] == "#" and image[i + ind_i][j + ind_j] != "#":
                return False
    return True


def count_monsters(image):
    count = 0
    for i in range(len(image) - hgt + 1):
        for j in range(len(image[0]) - wdt + 1):
            if spotted(i, j, image):
                count += 1
    return count


counts = []
for _ in range(4):
    counts.append(count_monsters(image))
    image = rotate(image)
image = flip(image)
for _ in range(4):
    counts.append(count_monsters(image))
    image = rotate(image)

assert counts.count(0) == len(counts) - 1

roughness = "\n".join(image).count("#") - max(counts) * "\n".join(monster).count("#")
print("Part Two:", roughness)
