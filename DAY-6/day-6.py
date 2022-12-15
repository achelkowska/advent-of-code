
signal = open("input.txt").readline().strip()

for i in range(4, len(signal)):
    code = list(signal[i-4:i])
    if len(set(code)) == 4:
        print("Part 1: ", i, " ", code)
        break

for i in range(14, len(signal)):
    code = list(signal[i-14:i])
    if len(set(code)) == 14:
        print("Part 2: ", i, " ", code)
        break


