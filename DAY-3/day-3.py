
def get_value(x):
    if x.islower():
        return ord(x)-96
    else:
        return ord(x)-38

priorities_sum = 0
index = 1
elves_team = []
team_priorities = 0

with open("input.txt") as inpt:
    for i in inpt:
        first_compartment = i.strip()[:int(len(i.strip())/2)]
        second_compartment = i.strip()[int(len(i.strip())/2):]
        misplaced = list(set(first_compartment).intersection(second_compartment))[0]
        priorities_sum += get_value(misplaced)
        if index%3 == 0:
            elves_team.append(i.strip())
            common = list((set(elves_team[0]).intersection(elves_team[1])).intersection(elves_team[2]))[0]
            team_priorities += get_value(common)
            elves_team = []
        else:
            elves_team.append(i.strip())
        index += 1
        

print("Part 1: ", priorities_sum)
print("Part 2: ", team_priorities)

