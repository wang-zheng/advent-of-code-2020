filepath = "input/21.txt"


ingredients = []
allergens = []


def parse(line):
    line = line[:-2]  # remove ")\n"
    part = line.split("(contains ")
    ingredient = part[0].strip().split(" ")
    allergen = part[1].strip().split(", ")
    return ingredient, allergen


with open(filepath) as fp:
    line = fp.readline()
    while line:
        ingredient, allergen = parse(line)
        ingredients.append(ingredient)
        allergens.append(allergen)
        line = fp.readline()

all_allergens = list(set([x for l in allergens for x in l]))
ingredient_map = {}
for x in all_allergens:
    list_of_sets = [
        set(ingredients[i]) for i in range(len(allergens)) if x in allergens[i]
    ]
    possible = set.intersection(*list_of_sets)
    ingredient_map[x] = possible

checked = []
while len(checked) != len(all_allergens):
    new = [x for x in all_allergens if x not in checked and len(ingredient_map[x]) == 1]
    for x in new:
        match = next(iter(ingredient_map[x]))
        for y in all_allergens:
            if x != y and match in ingredient_map[y]:
                ingredient_map[y].remove(match)
    checked.extend(new)

bad_ingredient = [next(iter(ingredient_map[x])) for x in all_allergens]
remain = [x for l in ingredients for x in l if x not in bad_ingredient]

print("Part One:", len(remain))

pairs = [(next(iter(ingredient_map[x])), x) for x in all_allergens]
pairs = sorted(pairs, key=lambda x: x[1])
bad_list = ",".join([x[0] for x in pairs])
print("Part Two:", bad_list)
