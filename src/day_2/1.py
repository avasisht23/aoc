file = open("input.txt", "r")
out = 0

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for line in file:
    parts = line.split(":")
    game_id = int(parts[0].split(" ")[1])

    events = parts[1].split(";")

    works = True
    for event in events:
        pulls = event.strip().split(",")

        for pull in pulls:
            [total, color] = pull.strip().split(" ")

            if int(total) > maxes[color]:
                works = False

    if works:
        out += game_id

print(out)
