def check_T_position(coord_a, coord_b):
    #return true if points are touching
    if abs(coord_a[0]-coord_b[0]) <= 1 and abs(coord_a[1] - coord_b[1]) <= 1:
        return True
    else:
        return False

def shift_point(coord_a, coord_b):
    if coord_a[0] == coord_b[0]: #move left/right
        if coord_a[1] > coord_b[1]: #right
            return [coord_b[0], coord_b[1]+1]
        elif coord_a[1] < coord_b[1]: #left
            return [coord_b[0], coord_b[1]-1]
    elif coord_a[1] == coord_b[1]: #move up/down
        if coord_a[0] > coord_b[0]: #up
            return [coord_b[0]+1, coord_b[1]]
        if coord_a[0] < coord_b[0]: #down
            return [coord_b[0]-1, coord_b[1]]
    else: # move diagonal
        if coord_a[0] > coord_b[0] and coord_a[1] > coord_b[1]: #up/right
            return [coord_b[0]+1, coord_b[1]+1]
        elif coord_a[0] < coord_b[0] and coord_a[1] > coord_b[1]: #down/right
            return [coord_b[0]-1, coord_b[1]+1]
        elif coord_a[0] > coord_b[0] and coord_a[1] < coord_b[1]: #up/left
            return [coord_b[0]+1, coord_b[1]-1]
        elif coord_a[0] < coord_b[0] and coord_a[1] < coord_b[1]: #down/left
            return [coord_b[0]-1, coord_b[1]-1]


## coords: 1 - ud, 2 - lr

def run_calc(nodes):
    directions = {"R": (0,1), "L":(0,-1), "U":(1,0), "D":(-1,0)}
    point_coords = [[0,0] for _ in range(nodes)] # 1st is head, and 1-9 tails
    nine_coords = [(0,0)]

    with open("input.txt") as inpt:
        for i in inpt:
            tab = i.strip().split()
            for moves in range(int(tab[1])):
                point_coords[0][0] += directions[tab[0]][0]
                point_coords[0][1] += directions[tab[0]][1]

                for t in range(1, len(point_coords)):
                    adjacent = check_T_position(point_coords[t-1], point_coords[t])
                    if not adjacent:
                        point_coords[t] = shift_point(point_coords[t-1], point_coords[t])
                nine_coords.append(tuple(point_coords[-1]))
    return nine_coords

print("Part 1: ", len(set(run_calc(2))))
print("Part 1: ", len(set(run_calc(10))))


