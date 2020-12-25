filepath = "input/25.txt"


def loop_size(key, subject=7):
    num = 1
    for i in range(100000000):
        num *= subject
        num = num % 20201227
        if num == key:
            break
    return i + 1


def gen_key(subject, loop_size):
    num = 1
    for i in range(loop_size):
        num *= subject
        num = num % 20201227
    return num


with open(filepath) as fp:
    line = fp.readline()
    card = int(line.strip())
    line = fp.readline()
    door = int(line.strip())


loop_card = loop_size(card)
encryption = gen_key(door, loop_card)


print("Part One:", encryption)
print("Part Two:", None)
