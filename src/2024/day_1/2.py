file = open("input.txt", "r")
out = 0

l1 = []
l2 = []

for line in file:
    [elt1, elt2] = line.strip().split()

    l1.append(int(elt1))
    l2.append(int(elt2))

m1 = {}

for i in range(len(l1)):
    m1[l1[i]] = 0

for i in range(len(l2)):
    if l2[i] in m1:
        m1[l2[i]] += 1

for i in range(len(l1)):
    out += l1[i] * m1[l1[i]]

file.close()
print(out)
