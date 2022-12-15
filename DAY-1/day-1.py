
max_sum = 0
elves_calories = []

with open("input.txt") as inpt:
    calories_sum = 0
    for i in inpt:
        if i == '\n':
            elves_calories.append(calories_sum)
            calories_sum = 0
        else:
            calories_sum += int(i.strip())
    elves_calories.append(calories_sum)
    calories_sum = 0

print("Part 1: ", max(elves_calories))
print("Part 2: ", sum(sorted(elves_calories, reverse=True)[:3]))
