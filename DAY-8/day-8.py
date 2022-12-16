
trees_visible = 0
map = []

with open("input.txt") as inpt:
    for i in inpt:
        map.append(list(i.strip()))


trees_visible += 2*len(map) + 2*(len(map)-2)

for row in range(1,len(map)-1):
    for column in range (1, len(map[0])-1):
        middle = map[row][column]
        left = map[row][0:column]
        right = map[row][column+1:]
        top = []
        down = []
        for r in range(0, row):
            top.append(map[r][column])
        for r in range(row+1, len(map)):
            down.append(map[r][column])
        
        if any(num >= middle  for num in left) and any(num >= middle  for num in right) and \
            any(num >= middle  for num in top) and any(num >= middle  for num in down):
            pass
        else:
            trees_visible += 1

print("Part 1: ", trees_visible)

max_score = 1
for row in range(1,len(map)-1):
    for column in range (1, len(map[0])-1):
        middle = map[row][column]
        left = map[row][0:column]
        right = map[row][column+1:]
        top = []
        down = []
        for r in range(0, row):
            top.append(map[r][column])
        for r in range(row+1, len(map)):
            down.append(map[r][column])
        score = 1
        for e, tree in enumerate(reversed(left)):
            if tree >= middle:
                score *= e+1
                break
            if e+1 == len(left):
                score *= e+1
        for e, tree in enumerate(right):
            if tree >= middle:
                score *= e+1
                break
            if e+1 == len(right):
                score *= e+1
        for e, tree in enumerate(reversed(top)):
            if tree >= middle:
                score *= e+1
                break
            if e+1 == len(top):
                score *= e+1
        for e, tree in enumerate(down):
            if tree >= middle:
                score *= e+1
                break
            if e+1 == len(down):
                score *= e+1
        if score > max_score:
            max_score = score

print("Part 2: ", max_score)
