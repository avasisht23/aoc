file = open("input.txt", "r")
out = 0

for line in file:
    levels = line.strip().split()
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    sign = 1
    is_valid = True
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        abs_diff = abs(diff)

        if diff == 0:
            is_valid = False
            break

        if i == 1:
            sign = diff // abs_diff

        if diff * sign < 0:
            is_valid = False
            break

        if abs_diff < 1 or abs_diff > 3:
            is_valid = False
            break

    if is_valid:
        out += 1

file.close()
print(out)
