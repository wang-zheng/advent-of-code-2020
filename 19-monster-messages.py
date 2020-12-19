filepath = "input/19.txt"


def parse(value):
    value = value.strip()
    if value == '"a"' or value == '"b"':
        return value[1]
    else:
        options = value.split("|")
        list_of_options = [
            [int(x) for x in option.strip().split(" ")] for option in options
        ]
        return list_of_options


rules = {}
messages = []
with open(filepath) as fp:
    line = fp.readline()
    while line.strip() != "":
        key, value = line.split(":")
        rules[int(key)] = parse(value)
        line = fp.readline()
    line = fp.readline()
    while line:
        messages.append(line.strip())
        line = fp.readline()


def check(string, rule_ind):
    rule = rules[rule_ind]
    if len(string) == 0:
        return False, ""
    if not isinstance(rule, list):
        valid = string[0] == rule
        remain = string[1:] if len(string) > 1 else ""
        return valid, remain
    for option in rule:
        part = string
        all_valid = True
        for num in option.copy():
            valid, part = check(part, num)
            if not valid:
                all_valid = False
                break
        if all_valid:
            return True, part
    return False, ""


count = 0
for message in messages:
    valid, remain = check(message, 0)
    if valid and remain == "":
        count += 1

print("Part One:", count)

# guess how many total times it repeats rules 42 or 31
repeat = int(max([len(message) for message in messages]) / 8)

rules[0] = []
rules[8] = []  # ignore these rules
rules[11] = []
for i in range(int(repeat / 2), 0, -1):  # find as many 31 as possible
    for j in range(repeat - 2 * i, 0, -1):  # find as many 42 as possible
        rules[0].append([42] * (i + j) + [31] * i)

count = 0
for message in messages:
    valid, remain = check(message, 0)
    if valid and remain == "":
        count += 1

print("Part Two:", count)
