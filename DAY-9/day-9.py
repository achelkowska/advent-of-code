
H = [0,0]
T = [0,0]


def check_HT_distance(tail, head):
    if head == tail:
        return "s"
    elif head[0] == tail[0] and abs(head[1]-tail[1]) <= 1:
        return "lr"
    elif head[1] == tail[1] and abs(head[0]-tail[0]) <= 1:
        return("ud")
    elif abs(head[1]-tail[1]) <= 1 and abs(head[0]-tail[0]) <= 1:
        return("c")
    else:
        return("shift")

def move_tail(tail, pos, head):
    if pos == "s":
        pass
    elif pos == "lr":
        if abs(head[1]-tail[1]+1) < abs(head[1]-tail[1]-1):
            return [tail[0], tail[1]-1]
        else:
            return [tail[0], tail[1]+1]
    elif pos == "ud":
        if abs(head[0]-tail[0]+1) < abs(head[0]-tail[0]-1):
            return [tail[0]-1, tail[1]]
        else:
            return [tail[0]+1, tail[1]]
    elif pos == "c":
        if abs(head[1]-tail[1]+1) < abs(head[1]-tail[1]-1):
            if abs(head[0]-tail[0]+1) < abs(head[0]-tail[0]-1): #left-down
                return [tail[0]-1, tail[1]-1]
            else: #left-top
                return [tail[0]+1, tail[1]-1]
        else:
            if abs(head[0]-tail[0]+1) < abs(head[0]-tail[0]-1): #right-down
                return [tail[0]-1, tail[1]+1]
            else: # right-top
                return [tail[0]+1, tail[1]+1]
    else:
        print("else: ", head, tail, pos)
    
tail_positions_final = [[0,0]]
temp_positions = []
with open("input.txt") as inpt:
    for i in inpt:
        tab = i.strip().split()
        if tab[0] == "R": #move head to right
            for _ in range(0,int(tab[1])):
                H[1] += 1
                pos = check_HT_distance(T, H)
                temp_positions.append(pos)
                if pos != "shift":
                    pass
                else:
                    for p in reversed(temp_positions):
                        if p != "shift":
                            pos = p
                            break
                    T = move_tail(T, pos, H)
                    pos = check_HT_distance(T, H)
                    temp_positions.append(pos)
                    if T not in tail_positions_final:
                        tail_positions_final.append(T)
        elif tab[0] == "U": #move head to up
            for _ in range(0,int(tab[1])):
                H[0] += 1
                pos = check_HT_distance(T, H)
                temp_positions.append(pos)
                if pos != "shift":
                    pass
                else:
                    for p in reversed(temp_positions):
                        if p != "shift":
                            mv = p
                            break
                    T = move_tail(T, mv, H)
                    pos = check_HT_distance(T, H)
                    temp_positions.append(pos)
                    if T not in tail_positions_final:
                        tail_positions_final.append(T)
        elif tab[0] == "L": #move head to left
            for _ in range(0,int(tab[1])):
                H[1] -= 1
                pos = check_HT_distance(T, H)
                temp_positions.append(pos)
                if pos != "shift":
                    pass
                else:
                    for p in reversed(temp_positions):
                        if p != "shift":
                            mv = p
                            break
                    T = move_tail(T, mv, H)
                    pos = check_HT_distance(T, H)
                    temp_positions.append(pos)
                    if T not in tail_positions_final:
                        tail_positions_final.append(T)
        elif tab[0] == "D": #move head to down
            for _ in range(0,int(tab[1])):
                H[0] -= 1
                pos = check_HT_distance(T, H)
                temp_positions.append(pos)
                if pos != "shift":
                    pass
                else:
                    for p in reversed(temp_positions):
                        if p != "shift":
                            mv = p
                            break
                    T = move_tail(T, mv, H)
                    pos = check_HT_distance(T, H)
                    temp_positions.append(pos)
                    if T not in tail_positions_final:
                        tail_positions_final.append(T)

print("Part 1: ", len(tail_positions_final))
