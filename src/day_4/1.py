file = open("input.txt", "r")
out = 0

for line in file:
    parts = line.split(":")[1]
    cards = parts.strip().split("|")

    winning_nums = set(cards[0].strip().split())
    your_nums = cards[1].strip().split()

    sum = 0
    i = 0
    for w in your_nums:
        if w in winning_nums:
            sum = 2**i
            i += 1

    out += sum

print(out)
