filepath = "input/18.txt"

equations = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        equation = line.strip().replace("(", "( ").replace(")", " )").split(" ")
        for i in range(len(equation)):
            if equation[i].isdigit():
                equation[i] = int(equation[i])
        equations.append(equation)
        line = fp.readline()


def evaluate_1(equation):
    if "(" not in equation:
        num = equation[0]
        for op, val in zip(equation[1::2], equation[2::2]):
            if op == "+":
                num += val
            elif op == "*":
                num *= val
        return num
    else:
        right_ind = equation.index(")")
        length = equation[right_ind::-1].index("(")
        left_ind = right_ind - length
        part = equation[left_ind + 1 : right_ind]
        value = evaluate_1(part)
        new = equation[:left_ind] + [value] + equation[right_ind + 1 :]
        return evaluate_1(new)


print("Part One:", sum([evaluate_1(equation) for equation in equations]))


def evaluate_2(equation):
    if "(" not in equation:
        if "+" in equation:
            ind = equation.index("+")
            value = equation[ind - 1] + equation[ind + 1]
            new = equation[: ind - 1] + [value] + equation[ind + 2 :]
            return evaluate_2(new)
        else:
            num = equation[0]
            for op, val in zip(equation[1::2], equation[2::2]):
                if op == "+":
                    num += val
                elif op == "*":
                    num *= val
            return num
    else:
        right_ind = equation.index(")")
        length = equation[right_ind::-1].index("(")
        left_ind = right_ind - length
        part = equation[left_ind + 1 : right_ind]
        value = evaluate_2(part)
        new = equation[:left_ind] + [value] + equation[right_ind + 1 :]
        return evaluate_2(new)


print("Part Two:", sum([evaluate_2(equation) for equation in equations]))
