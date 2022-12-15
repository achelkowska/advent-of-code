
def stack_parser(lines):
    stack_strings = []
    for l in lines:
        for e, j in enumerate("".join(l.split("   ")).split(" ")):
            if j != "":
                if len(stack_strings) > e:
                    stack_strings[e].append(j[1:2])
                else:
                    stack_strings.append([j[1:2]])
            else:
                if len(stack_strings) <= e:
                    stack_strings.append([])
    for s in stack_strings:
        s.reverse()
    return stack_strings

def print_stack(st):
    for e, x in enumerate(st):
        print(e+1, " ", x)


## Part 1, single crate move
top = ""
with open("input.txt") as inpt:
    stack_lines = []
    for i in inpt:
        if not i.startswith("move") and not i.startswith(" 1"):
            stack_lines.append(i.strip())
        else:
            stack = stack_parser(stack_lines)
            break
    for i in inpt:
        if i.startswith("move"):
            # ile skad gdzie
            step = [int(i.split()[1]), int(i.split()[3]), int(i.split()[5])]
            for _ in range(0, step[0]):
                x = stack[step[1]-1].pop()
                stack[step[2]-1].append(x)
    for i in stack:
        top += i[-1]

print("Part 1: ", top)


## Part 2, stacked crates move
top = ""
with open("input.txt") as inpt:
    stack_lines = []
    for i in inpt:
        if not i.startswith("move") and not i.startswith(" 1"):
            stack_lines.append(i.strip())
        else:
            stack = stack_parser(stack_lines)
            break
    for i in inpt:
        if i.startswith("move"):
            # ile skad gdzie
            step = [int(i.split()[1]), int(i.split()[3]), int(i.split()[5])]
            for y in range(0-step[0], 0):
                x = stack[step[1]-1].pop(y)
                stack[step[2]-1].extend(x)
    for i in stack:
        top += i[-1]

print("Part 2: ", top)


            
