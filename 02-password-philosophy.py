def is_valid_1(num, char, password):
    count = password.count(char)
    return count >= num[0] and count <= num[1]


def is_valid_2(num, char, password):
    if password[num[0] - 1] == char and not password[num[1] - 1] == char:
        return True
    if not password[num[0] - 1] == char and password[num[1] - 1] == char:
        return True
    return False


filepath = "input/02.txt"
valid_1 = 0
valid_2 = 0
with open(filepath) as fp:
    line = fp.readline()
    while line:
        chunk = line.split()
        num = [int(x) for x in chunk[0].split("-")]
        char = chunk[1][0]
        password = chunk[2]
        if is_valid_1(num, char, password):
            valid_1 += 1
        if is_valid_2(num, char, password):
            valid_2 += 1
        line = fp.readline()

print("Part One:", valid_1)
print("Part Two:", valid_2)
