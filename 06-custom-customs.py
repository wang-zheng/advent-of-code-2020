filepath = "input/06.txt"


def count_1(str):
    count = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        in_one = False
        for line in str:
            if c in line:
                in_one = True
        if in_one:
            count += 1
    return count


def count_2(str):
    count = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        in_all = True
        for line in str:
            if c not in line:
                in_all = False
        if in_all:
            count += 1
    return count


total_1 = 0
total_2 = 0
group = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        if line.strip() != "":
            group.append(line.strip())
        else:
            total_1 += count_1(group)
            total_2 += count_2(group)
            group = []

        line = fp.readline()

total_1 += count_1(group)
total_2 += count_2(group)

print("Part One:", total_1)
print("Part Two:", total_2)
