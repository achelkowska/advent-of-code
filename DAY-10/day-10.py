
cycle_no = 0
X = 1
cycle_record = {}
matrix = [["." for _ in range(40)]]
sprite_pos = [0, 1, 2]
print_cycle = -1
row = 0

def switch_row(cycle, row, matrix):
    if cycle >= 40:
        cycle -= 40
        row += 1
        matrix.append(["." for _ in range(40)])
    return cycle, row, matrix


with open("input.txt") as inpt:
    for i in inpt:
        tab = i.strip().split()
        if tab[0] == "noop":
            cycle_no += 1
            cycle_record[cycle_no] = X
            print_cycle += 1
            print_cycle, row, matrix = switch_row(print_cycle, row, matrix)
            if print_cycle in sprite_pos: matrix[row][print_cycle] = "#"
        elif tab[0] == "addx":
            cycle_no += 1
            cycle_record[cycle_no] = X
            print_cycle += 1
            print_cycle, row, matrix = switch_row(print_cycle, row, matrix)
            if print_cycle in sprite_pos: matrix[row][print_cycle] = "#"
            cycle_no += 1
            cycle_record[cycle_no] = X
            print_cycle += 1
            print_cycle, row, matrix = switch_row(print_cycle, row, matrix)
            if print_cycle in sprite_pos: matrix[row][print_cycle] = "#"
            X += int(tab[1])
            sprite_pos = [X-1, X, X+1]


result = [20, 60, 100, 140, 180, 220]
tot_sum = 0
for r in result:
    tot_sum += cycle_record[r] * r

print("Part 1: ", tot_sum)
print("Part 2:")
for row in matrix:
    print("".join(row))



