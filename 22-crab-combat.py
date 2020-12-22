filepath = "input/22.txt"


player_1 = []
player_2 = []

with open(filepath) as fp:
    line = fp.readline()
    assert line.strip() == "Player 1:"
    line = fp.readline()
    while line.strip() != "":
        card = int(line.strip())
        player_1.append(card)
        line = fp.readline()

    line = fp.readline()
    assert line.strip() == "Player 2:"
    line = fp.readline()
    while line:
        card = int(line.strip())
        player_2.append(card)
        line = fp.readline()


def round(player_1, player_2):
    cards = [player_1.pop(0), player_2.pop(0)]
    if cards[0] > cards[1]:
        player_1.extend(cards)
    else:
        player_2.extend(cards[::-1])


player_1_copy = player_1.copy()
player_2_copy = player_2.copy()

while len(player_1) > 0 and len(player_2) > 0:
    round(player_1, player_2)

score = 0
for i, card in enumerate(player_1[::-1] + player_2[::-1]):
    score += (i + 1) * card

print("Part One:", score)


def recursive_round(player_1, player_2):
    cards = [player_1.pop(0), player_2.pop(0)]
    if len(player_1) >= cards[0] and len(player_2) >= cards[1]:
        new_1 = player_1[: cards[0]].copy()
        new_2 = player_2[: cards[1]].copy()
        winner, _ = recursive_combat(new_1, new_2)
    else:
        winner = "Player 1" if cards[0] > cards[1] else "Player 2"

    if winner == "Player 1":
        player_1.extend(cards)
    elif winner == "Player 2":
        player_2.extend(cards[::-1])
    else:
        raise Exception("Who won?")


def recursive_combat(player_1, player_2):
    cache = []
    while len(player_1) > 0 and len(player_2) > 0:
        cache.append((player_1.copy(), player_2.copy()))
        recursive_round(player_1, player_2)
        if (player_1, player_2) in cache:
            return "Player 1", player_1

    if len(player_1) > len(player_2):
        return "Player 1", player_1
    else:
        return "Player 2", player_2


player_1 = player_1_copy
player_2 = player_2_copy
_, deck = recursive_combat(player_1, player_2)

score = 0
for i, card in enumerate(deck[::-1]):
    score += (i + 1) * card

print("Part Two:", score)
