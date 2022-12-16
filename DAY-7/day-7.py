
directories = {"/":0}
current_dir = []
cnt = 0

with open("input.txt") as inpt:
    for i in inpt:
        tab = i.strip().split()
        if tab[0] == "$":
            if tab[1] == "cd" and tab[2] != "..":
                current_dir.append(tab[2])
            elif tab[1] == "ls":
                pass
            elif tab[1] == "cd" and tab[2] == "..":
                current_dir.pop()
        elif tab[0] == "dir":
            path = ""
            for d in current_dir:
                path += "_"+d
                if path in directories:
                    pass
                else:
                    directories[path] = 0
            directories[path+"_"+tab[1]] = 0
            
        else:
            path = ""
            for d in current_dir:
                path += "_"+d
                if path in directories:
                    directories[path] += int(tab[0])
                else:
                    print("error")
                    print(path)
                

dir_sum = 0
for d in directories:
    if directories[d] <= 100000:
        #print(d, directories[d])
        dir_sum += directories[d]

print("Part 1: ", dir_sum)
max_dir = max(directories.values())
free = 70000000 - max_dir

for d in dict(sorted(directories.items(), key=lambda item: item[1])):
    if directories[d] + free  >= 30000000:
        print("Part 2: ", d.split("_")[-1], directories[d])
        break


    


