file = open("input.txt", "r")
out = 0

graph = {}
queue = []

for line in file:
    parts = line.split(":")
    card_id = int(parts[0].strip().split()[1])

    cards = parts[1].strip().split("|")

    winning_nums = set(cards[0].strip().split())
    your_nums = cards[1].strip().split()

    copies = []
    i = card_id
    for w in your_nums:
        if w in winning_nums:
            i += 1
            copies.append(i)

    graph[card_id] = copies
    queue.extend(copies)

    out += 1

while queue:
    card_id = queue.pop(0)
    out += 1

    if card_id not in graph:
        continue

    if len(graph[card_id]) == 0:
        continue

    queue.extend(graph[card_id])

print(out)
