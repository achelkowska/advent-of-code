complete_overlaps = 0
overlaps_count = 0

with open("input.txt") as inpt:
    for i in inpt:
        tab = i.strip().split(",")
        a_tasks = list(range(int(tab[0].split("-")[0]),int(tab[0].split("-")[1])+1))
        b_tasks = list(range(int(tab[1].split("-")[0]),int(tab[1].split("-")[1])+1))
        overlap = sorted(list(set(a_tasks).intersection(b_tasks)))
        if overlap:
            overlaps_count += 1
            if overlap == a_tasks or overlap == b_tasks:
                complete_overlaps += 1
        

print("Part 1: ", complete_overlaps)
print("Part 2: ", overlaps_count)