file = open("input.txt", "r")
out = 0

def check_is_valid(levels):
    is_increasing = levels[0] < levels[1]
    for i in range(1, len(levels)):
        new_is_increasing = levels[i - 1] < levels[i]
        abs_diff = abs(levels[i] - levels[i - 1])

        if is_increasing != new_is_increasing or abs_diff < 1 or abs_diff > 3:
            return False

    return True

for line in file:
    levels = line.strip().split()
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    is_valid = check_is_valid(levels)
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        is_valid = is_valid or check_is_valid(new_levels)

    if is_valid:
        out += 1

file.close()
print(out)
