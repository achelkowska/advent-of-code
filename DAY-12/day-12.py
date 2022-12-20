
se_positions = [[], []] # start, end || u/d, r/l
matrix = []

with open("input.txt") as inpt:
    for i in inpt:
        row = []
        for e, letter in enumerate(list(i.strip())):
            if letter == "S": 
                se_positions[0] = [len(matrix), e]
                row.append('a')
            elif letter == "E": 
                se_positions[1] = [len(matrix), e]
                row.append('z')
            else:
                row.append(letter)
        matrix.append(row)

movement = []

directions = ((0,-1), (+1,0), (0,+1), (-1,0)) # l,u,r,d

for row in range(len(matrix)):
    movement.append([])
    movement[-1] = [[] for _ in range(len(matrix[0]))]
    for column in range(len(matrix[0])):
        for d in directions:
            if row + d[0] >= 0 and column + d[1] >= 0 and row + d[0] < len(matrix) and column + d[1] < len(matrix[row]):
                if ord(matrix[row][column])+1 >= ord(matrix[row+d[0]][column+d[1]]):
                    movement[row][column].append([d[0], d[1]])


graph = {}

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        graph[(row, column)] = []
        for move in movement[row][column]:
            graph[(row, column)].append((row+move[0], column+move[1]))

def BFS(graph, n1, n2):
    path_list = [[n1]]
    path_index = 0
   
    previous_nodes = {n1}
    if n1 == n2: 
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        
        if n2 in next_nodes:
            current_path.append(n2)
            return current_path
        
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                
                previous_nodes.add(next_node)
        
        path_index += 1
   
    return []


x = BFS(graph, tuple(se_positions[0]), tuple(se_positions[1]))
print("Part 1: ", len(x)-1)

paths = {}
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == "a":
            x = BFS(graph, (row, column), tuple(se_positions[1]))
            paths[(row, column)] = len(x)-1


for p in sorted(paths.values()):
    if p > -1:
        print("Part 2: ", list(paths.keys())[list(paths.values()).index(p)], p)
        break







