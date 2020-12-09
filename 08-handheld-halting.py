def execute_recursive(program, i, visited, accumulator=0):
    if i in visited:
        return (accumulator, False)
    elif i == len(program):
        return (accumulator, True)
    elif i > len(program) or i < 0:
        return (accumulator, False)
    else:
        visited.append(i)
        operation = program[i][:3]
        argument = int(program[i][4:])
        if operation == "acc":
            accumulator += argument
            i += 1
        elif operation == "jmp":
            i += argument
        elif operation == "nop":
            i += 1
        return execute_recursive(program, i, visited, accumulator)


filepath = "input/08.txt"

program = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        program.append(line)
        line = fp.readline()

visited = []
print("Part One:", execute_recursive(program, 0, visited)[0])

for i in visited:
    line = program[i]
    if line[:3] == "nop":
        program[i] = line.replace("nop", "jmp")
    elif line[:3] == "jmp":
        program[i] = line.replace("jmp", "nop")
    else:
        continue

    fresh_visited = []
    ans = execute_recursive(program, 0, fresh_visited)
    if ans[1]:
        print("Part Two:", ans[0])
        break

    program[i] = line
