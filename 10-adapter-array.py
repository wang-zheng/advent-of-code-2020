filepath = "input/10.txt"

adapters = [0]

with open(filepath) as fp:
    line = fp.readline()
    while line:
        adapters.append(int(line))
        line = fp.readline()

adapters = sorted(adapters)
diff = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
count_1 = len([x for x in diff if x == 1])
count_3 = len([x for x in diff if x == 3]) + 1

print("Part One:", count_1 * count_3)

mem = {}  # memory to store answers


def count_arrange(i, j, adapters, mem):
    if (i, j) in mem.keys():
        return mem[(i, j)]
    elif j < i or i < 0 or j >= len(adapters):
        mem[(i, j)] = 1
    elif j - i <= 1:  # base case solutions for small sizes
        assert adapters[j] - adapters[i] <= 3
        mem[(i, j)] = 1
    elif j - i == 2:
        if adapters[j] - adapters[i] <= 3:
            mem[(i, j)] = 2
        else:
            mem[(i, j)] = 1
    elif j - i == 3:
        count = 1
        if adapters[j] - adapters[i + 1] <= 3:
            count += 1
        if adapters[j - 1] - adapters[i] <= 3:
            count += 1
        if adapters[j] - adapters[i] <= 3:
            count += 1
        mem[(i, j)] = count
    elif adapters[j] - adapters[i] <= 3:
        mem[(i, j)] = 2 ** (j - i - 1)

    if (i, j) in mem.keys():
        return mem[(i, j)]

    k = round((i + j) / 2)  # roughly middle index
    count = count_arrange(i, k, adapters, mem) * count_arrange(k, j, adapters, mem)
    count += count_arrange(i, k + 1, adapters, mem) * count_arrange(
        k + 1, j, adapters, mem
    )
    count += count_arrange(i, k - 1, adapters, mem) * count_arrange(
        k - 1, j, adapters, mem
    )
    if adapters[k] - adapters[k - 1] <= 3:
        count -= count_arrange(i, k - 1, adapters, mem) * count_arrange(
            k, j, adapters, mem
        )
    if adapters[k + 1] - adapters[k] <= 3:
        count -= count_arrange(i, k, adapters, mem) * count_arrange(
            k + 1, j, adapters, mem
        )
    if adapters[k + 1] - adapters[k - 1] <= 3:
        count -= count_arrange(i, k - 1, adapters, mem) * count_arrange(
            k + 1, j, adapters, mem
        )
    mem[(i, j)] = count
    return count


print("Part Two:", count_arrange(0, len(adapters) - 1, adapters, mem))
