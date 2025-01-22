file = "input.txt"


def create_matrix():
    matrix = []
    with open(file) as f:
        for line in f:
            matrix.append(list(map(int, line.strip())))
    return matrix


def check_hiking_trail(matrix, i, j, next_to_find):
    res = 0
    if next_to_find == 10:
        res += 1
        return res

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if (
            0 <= ni < len(matrix)
            and 0 <= nj < len(matrix[i])
            and matrix[ni][nj] == next_to_find
        ):
            res += check_hiking_trail(matrix, ni, nj, next_to_find + 1)

    return res


def part1():
    res = 0
    matrix = create_matrix()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                res += check_hiking_trail(matrix, i, j, 1)
    print(res)


part1()
