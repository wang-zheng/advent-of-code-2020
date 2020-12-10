def check_pair(list, sum):
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                continue
            if list[i] + list[j] == sum:
                return True
    return False


def find_invalid(program, length=25):
    for i in range(length, len(program)):
        if not check_pair(program[i - length : i], program[i]):
            return program[i]
    return None


def find_set(program, num):
    for i in range(len(program)):
        total = program[i]
        for j in range(i + 1, len(program)):
            total += program[j]
            if total == num:
                return weakness(program[i : j + 1])
            elif total > num:
                break
    return None


def weakness(program):
    return min(program) + max(program)


filepath = "input/09.txt"

program = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        program.append(int(line))
        line = fp.readline()

part_1 = find_invalid(program)
print("Part One:", part_1)
print("Part Two:", find_set(program, part_1))
