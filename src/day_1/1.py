file = open("input.txt", "r")
out = 0

for line in file:
    first = None
    last = None

    for i in range(len(line)):
        l = i
        potential_first = line[i]

        if first is None and potential_first.isnumeric():
            first = int(potential_first)

        r = len(line) - i - 1
        potential_last = line[r]

        if last is None and potential_last.isnumeric():
            last = int(potential_last)

    out += 10 * first + last

file.close()
print(out)
