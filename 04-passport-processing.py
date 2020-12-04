filepath = "input/04.txt"


def valid_1(str):
    parts = str.split(" ")
    stems = [part.split(":")[0] for part in parts]
    for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if field not in stems:
            return False
    return True


def valid_2(str):
    if not valid_1(str):
        return False
    parts = str.split(" ")
    allstems = [part.split(":") for part in parts]

    byr = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "byr"][0]
    iyr = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "iyr"][0]
    eyr = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "eyr"][0]
    hgt = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "hgt"][0]
    hcl = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "hcl"][0]
    ecl = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "ecl"][0]
    pid = [allstems[i][1] for i in range(len(allstems)) if allstems[i][0] == "pid"][0]

    if not byr.isdigit() or int(byr) < 1920 or int(byr) > 2002:
        return False
    if not iyr.isdigit() or int(iyr) < 2010 or int(iyr) > 2020:
        return False
    if not eyr.isdigit() or int(eyr) < 2020 or int(eyr) > 2030:
        return False
    if not hgt[-2:] in ["cm", "in"] or not hgt[:-2].isdigit():
        return False
    if hgt[-2:] == "cm" and (int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193):
        return False
    if hgt[-2:] == "in" and (int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76):
        return False
    if hcl[0] != "#" or len(hcl) != 7:
        return False
    for c in hcl[1:]:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if c not in ["a", "b", "c", "d", "e", "f"]:
                return False
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not pid.isdigit() or len(pid) != 9:
        return False
    return True


passport = ""
total_1 = 0
total_2 = 0
with open(filepath) as fp:
    line = fp.readline()
    while line:
        if line.strip() != "":
            passport = passport + " " + line.strip()
        else:
            if valid_1(passport):
                total_1 += 1
            if valid_2(passport):
                total_2 += 1
            passport = ""
        line = fp.readline()

    if valid_1(passport):
        total_1 += 1
    if valid_2(passport):
        total_2 += 1

print("Part One:", total_1)
print("Part Two:", total_2)
