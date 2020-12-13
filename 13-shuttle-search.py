filepath = "input/13.txt"

with open(filepath) as fp:
    line = fp.readline()
    time = int(line.strip())
    line = fp.readline()
    buses = [int(time) for time in line.split(",") if time != "x"]

best = None
best_bus = None
for bus in buses:
    wait = (bus - (time % bus)) % bus
    if best is None or wait < best:
        best = wait
        best_bus = bus

print("Part One:", best * best_bus)

ordered_buses = [
    (-pos, int(time)) for pos, time in enumerate(line.split(",")) if time != "x"
]
ordered_buses = sorted(ordered_buses, key=lambda x: x[1])


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


def merge(big, small):
    test = big[0]
    valid = False
    while not valid:
        test += big[1]
        valid = (test - small[0]) % small[1] == 0

    return test, lcm(big[1], small[1])


temp = ordered_buses[0]
for i in range(1, len(ordered_buses)):
    temp = merge(temp, ordered_buses[i])

print("Part Two:", temp[0])
