filepath = "input/23.txt"


with open(filepath) as fp:
    line = fp.readline()
    cups = [int(x) for x in line.strip()]


llist = {}
size = len(cups)
for i in range(size - 1):
    llist[cups[i]] = cups[i + 1]
llist[cups[-1]] = cups[0]


def next(llist, i, n):
    ans = []
    for _ in range(n):
        i = llist[i]
        ans.append(i)
    return ans


def next_three(llist, i):
    pick_up = next(llist, i, 3)
    llist[i] = llist[pick_up[-1]]
    return pick_up


def destination(current, pick_up):
    current -= 1
    current = size if current == 0 else current
    while current in pick_up:
        current -= 1
        current = size if current == 0 else current

    return current


def move(current):
    pick_up = next_three(llist, current)
    j = destination(current, pick_up)
    end = llist[j]
    llist[j] = pick_up[0]
    llist[pick_up[-1]] = end
    return llist[current]


current = cups[0]
for _ in range(10):
    current = move(current)

ans = next(llist, 1, 8)

print("Part One:", "".join([str(x) for x in ans]))

llist = {}
size = 1000000
for i in range(len(cups) - 1):
    llist[cups[i]] = cups[i + 1]
llist[cups[-1]] = len(cups) + 1
for i in range(len(cups) + 1, size):
    llist[i] = i + 1
llist[size] = cups[0]

current = cups[0]
for _ in range(10000000):
    current = move(current)

ans = next(llist, 1, 2)

print("Part Two:", ans[0] * ans[1])
