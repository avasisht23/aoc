file = open("input.txt", "r")

visited = set({})
matrix = []
special_chars = set({})
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for line in file:
    chars = list(line.strip())
    matrix.append(chars)

    for char in chars:
        if char.isnumeric() or char is ".":
            continue

        special_chars.add(char)

out = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] not in special_chars:
            continue

        for d in dirs:
            x = i + d[0]
            y = j + d[1]

            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[i]):
                continue

            if matrix[x][y] == ".":
                continue

            if (x, y) not in visited and matrix[x][y].isnumeric():
                num = matrix[x][y]
                visited.add((x, y))

                l = -1
                while (
                    y + l >= 0
                    and matrix[x][y + l].isnumeric()
                    and (x, y + l) not in visited
                    and matrix[x][y + l] not in special_chars
                ):
                    num = matrix[x][y + l] + num
                    visited.add((x, y + l))
                    l -= 1

                r = 1
                while (
                    y + r < len(matrix[i])
                    and matrix[x][y + r].isnumeric()
                    and (x, y + r) not in visited
                    and matrix[x][y + r] not in special_chars
                ):
                    num = num + matrix[x][y + r]
                    visited.add((x, y + r))
                    r += 1

                out += int(num)

print(out)
