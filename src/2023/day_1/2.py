file = open("input.txt", "r")
out = 0

spelled_out = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_num(line: str, reverse: bool) -> int:
    for i in range(len(line)):
        if line[i].isnumeric():
            return int(line[i])

        for j in range(0, 6):
            if i + j >= len(line):
                break

            potential = line[i : (i + j)]
            if reverse:
                potential = potential[::-1]

            if potential in spelled_out:
                return spelled_out[potential]

    raise Exception("number not found")


for line in file:
    first = find_num(line, False)
    last = find_num(line[::-1], True)

    out += 10 * first + last

file.close()
print(out)
