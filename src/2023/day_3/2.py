file = open("input.txt", "r")

visited = set({})
matrix = []
special_char = "*"
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for line in file:
    chars = list(line.strip())
    matrix.append(chars)

out = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != special_char:
            continue

        parts = []
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
                    and matrix[x][y + l] != special_char
                ):
                    num = matrix[x][y + l] + num
                    visited.add((x, y + l))
                    l -= 1

                r = 1
                while (
                    y + r < len(matrix[i])
                    and matrix[x][y + r].isnumeric()
                    and (x, y + r) not in visited
                    and matrix[x][y + r] != special_char
                ):
                    num = num + matrix[x][y + r]
                    visited.add((x, y + r))
                    r += 1

                parts.append(num)

        if len(parts) != 2:
            continue

        out += int(parts[0]) * int(parts[1])

print(out)
