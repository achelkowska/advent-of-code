strategy = {"A X":4, "A Y":8, "A Z":3,
            "B X":1, "B Y":5, "B Z":9,
            "C X":7, "C Y":2, "C Z":6}

correct_strategy = {"A X":3, "A Y":4, "A Z":8,
                    "B X":1, "B Y":5, "B Z":9,
                    "C X":2, "C Y":6, "C Z":7}

guide_score = 0
correct_score = 0
with open("input.txt") as inpt:
    for i in inpt:
        guide_score += strategy[i.strip()]
        correct_score += correct_strategy[i.strip()]

print("Part 1: ", guide_score)
print("Part 2: ", correct_score)