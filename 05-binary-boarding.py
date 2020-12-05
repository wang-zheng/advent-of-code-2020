filepath = "input/05.txt"


def to_dec(bin):
    dec = 0
    for i in bin:
        dec = dec * 2
        dec = dec + int(i)
    return dec


def seat_id(ticket):
    ticket = ticket.replace("F", "0")
    ticket = ticket.replace("B", "1")
    ticket = ticket.replace("R", "1")
    ticket = ticket.replace("L", "0")
    row = to_dec(ticket[:7])
    col = to_dec(ticket[7:])
    return row * 8 + col


all_ids = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        ticket = line.strip()
        num = seat_id(ticket)
        all_ids.append(num)
        line = fp.readline()

all_ids.sort()
seat = [i + 1 for i in all_ids if i + 1 not in all_ids][0]

print("Part One:", max(all_ids))
print("Part Two:", seat)
