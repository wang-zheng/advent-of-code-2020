filepath = "input/03.txt"
area = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        area.append(line.strip())
        line = fp.readline()


def traverse(area, right, down=1):
    N = len(area[0])
    M = len(area)
    trees = 0
    x = 0
    y = 0
    while x < M:
        if area[x][y] == "#":
            trees += 1
        y = (y + right) % N
        x = x + down
    return trees


print("Part One:", traverse(area, 3))

part_two = (
    traverse(area, 1)
    * traverse(area, 3)
    * traverse(area, 5)
    * traverse(area, 7)
    * traverse(area, 1, 2)
)

print("Part Two:", part_two)
