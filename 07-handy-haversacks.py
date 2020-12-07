import re


def parse(line):
    parts = re.split(f"bags contain|no other|bags|bag|,|\.", line)
    parts = [part.strip() for part in parts if part.strip() != ""]
    return parts


rules = {}


def recursive_check(mem, bag, gold="shiny gold"):
    if bag in mem.keys():
        return mem[bag]
    if bag == "shiny gold":
        return True
    for subbag in rules[bag]:
        subbag = re.sub("\d+", "", subbag).strip()
        if recursive_check(mem, subbag, gold):
            mem[bag] = True
            return True
    mem[bag] = False
    return False


def recursive_count(mem, bag):
    if bag in mem.keys():
        return mem[bag]
    total = 0
    for subbag in rules[bag]:
        number = int(re.split(" ", subbag)[0])
        subbag = re.sub("\d+", "", subbag).strip()
        total += number * (recursive_count(mem, subbag) + 1)
    mem[bag] = total
    return total


filepath = "input/07.txt"

with open(filepath) as fp:
    line = fp.readline()
    while line:
        parts = parse(line)
        rules[parts[0]] = parts[1:]
        line = fp.readline()

valid = 0
mem1 = {}
for bag in rules.keys():
    if recursive_check(mem1, bag):
        valid += 1

mem2 = {}
print("Part One:", valid)
print("Part Two:", recursive_count(mem2, "shiny gold"))
