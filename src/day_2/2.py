from functools import reduce

file = open("input.txt", "r")
out = 0

for line in file:
    parts = line.split(":")

    events = parts[1].split(";")

    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    works = True
    for event in events:
        pulls = event.strip().split(",")

        for pull in pulls:
            [total, color] = pull.strip().split(" ")

            if int(total) > mins[color]:
                mins[color] = int(total)

    out += reduce(lambda arr, x: arr * x, mins.values())

print(out)
