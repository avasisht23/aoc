file = open("input.txt", "r")
out = 0

l1 = []
l2 = []

for line in file:
    [elt1, elt2] = line.strip().split()

    l1.append(int(elt1))
    l2.append(int(elt2))

l1.sort()
l2.sort()

for i in range(len(l1)):
    out += abs(l1[i] - l2[i])

file.close()
print(out)
