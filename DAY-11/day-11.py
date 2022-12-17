def run_monkeys(part, n):
    with open("input.txt") as inpt:
        monkey_items = []
        monkey_operations = [] # lambda 23 T-2 F-3
        monkey_inspections = []
        rounds = n
        for i in inpt:
            tab = i.strip().replace(",", "").split()
            if tab:
                if tab[0] == "Monkey":
                    monkey_items.append([])
                    monkey_operations.append([])
                    monkey_inspections.append(0)
                elif tab[0] == "Starting":
                    for item in tab[2:]:
                        monkey_items[-1].append(int(item))  
                elif tab[0] == "Operation:":
                    if tab[4] == "*":
                        if tab[5] != "old":
                            monkey_operations[-1].append(eval("lambda old: old * {}".format(tab[5])))
                        else:
                            monkey_operations[-1].append(eval("lambda old: old * old"))
                    elif tab[4] == "+":
                        monkey_operations[-1].append(eval("lambda old: old + {}".format(tab[5])))
                elif tab[0] == "Test:":
                    monkey_operations[-1].append(int(tab[3]))
                elif tab[1] == "true:":
                    monkey_operations[-1].append(int(tab[5]))
                elif tab[1] == "false:":
                    monkey_operations[-1].append(int(tab[5]))

    group_modulo = 1
    for monkey in monkey_operations:
        group_modulo *= monkey[1]

    for _ in range(rounds):
        #print(_)
        for monkey in range(len(monkey_items)):
            for i in range(len(monkey_items[monkey])):
                monkey_inspections[monkey] += 1
                item = monkey_items[monkey].pop(0)
                if part == 1:
                    item = (monkey_operations[monkey][0](item)) // (5-2*part)
                else:
                    item = (monkey_operations[monkey][0](item) % group_modulo) // (5-2*part)
                if item % monkey_operations[monkey][1] == 0:
                    monkey_items[monkey_operations[monkey][2]].append(item)
                else:
                    monkey_items[monkey_operations[monkey][3]].append(item)
    return monkey_inspections

monkey_inspections = run_monkeys(1, 20)
print("Part 1: ", sorted(monkey_inspections)[-1]*sorted(monkey_inspections)[-2])

monkey_inspections = run_monkeys(2, 10000)
print("Part 2: ", sorted(monkey_inspections)[-1]*sorted(monkey_inspections)[-2])

          