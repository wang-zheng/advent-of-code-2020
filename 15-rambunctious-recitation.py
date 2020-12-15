import re

filepath = "input/15.txt"

with open(filepath) as fp:
    line = fp.readline()
    nums = [int(x) for x in line.split(",")]

mem = {}
for i, n in enumerate(nums[:-1]):
    mem[n] = i + 1
last = nums[-1]
index = len(nums) + 1


def apply(mem, index, last):
    if last in mem.keys():
        diff = index - mem[last] - 1
    else:
        diff = 0
    mem[last] = index - 1
    return diff


end = 2020

for i in range(index, end + 1):
    last = apply(mem, i, last)

print("Part One:", last)

mem = {}
for i, n in enumerate(nums[:-1]):
    mem[n] = i + 1
last = nums[-1]
index = len(nums) + 1

end = 30000000

for i in range(index, end + 1):
    last = apply(mem, i, last)

print("Part Two:", last)
