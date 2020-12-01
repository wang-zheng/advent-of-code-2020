def find_entries(arr, start, end, match=2020):
    i = start
    j = end
    total = arr[i] + arr[j]

    while total != match:
        if total < match:
            i = i + 1
        elif total > match:
            j = j - 1
        total = arr[i] + arr[j]

        if i >= j:
            return None

    return (arr[i], arr[j])


filepath = "input/01.txt"
arr = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        arr.append(int(line))
        line = fp.readline()

arr.sort()
(first, second) = find_entries(arr, 0, len(arr) - 1)

print("Part One:", first * second)

for i in range(0, len(arr) - 2):
    remain = 2020 - arr[i]
    ans = find_entries(arr, i + 1, len(arr) - 1, remain)
    if ans is not None:
        first = arr[i]
        (second, third) = ans
        break

print("Part Two:", first * second * third)
