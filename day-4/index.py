file = "input.txt"


def create_matrix():
    with open(file, "r") as f:
        return [list(line.strip()) for line in f]


WORD_TO_SEARCH = ["X", "M", "A", "S"]
DIRECTIONS = {
    "diagonal": [(1, 1), (-1, -1)],
    "reverse-diagonal": [(1, -1), (-1, 1)],
    "vertical": [(1, 0), (-1, 0)],
    "horizontal": [(0, 1), (0, -1)],
}


def search_possible_path(matrix, i, j, current_char_index, direction):
    max_i, max_j, res = len(matrix), len(matrix[0]), 0
    for di, dj in DIRECTIONS[direction]:
        ni, nj = i + di, j + dj
        if (
            0 <= ni < max_i
            and 0 <= nj < max_j
            and matrix[ni][nj] == WORD_TO_SEARCH[current_char_index]
        ):
            if current_char_index == len(WORD_TO_SEARCH) - 1:
                res += 1
            else:
                res += search_possible_path(
                    matrix, ni, nj, current_char_index + 1, direction
                )
    return res


def part1():
    matrix = create_matrix()
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "X":
                for key in DIRECTIONS:
                    res += search_possible_path(matrix, i, j, 1, key)
    print(res)


POSSIBLE_VARIANTES = [("S", "M"), ("M", "S")]


def is_MAS_square(matrix, i, j):
    max_i, max_j = len(matrix), len(matrix[0])
    for direction in ["diagonal", "reverse-diagonal"]:
        possible_chars = {"S", "M"}
        for di, dj in DIRECTIONS[direction]:
            ni, nj = i + di, j + dj
            if 0 <= ni < max_i and 0 <= nj < max_j and matrix[ni][nj] in possible_chars:
                possible_chars.remove(matrix[ni][nj])
            else:
                return False
    return True


def part2():
    matrix = create_matrix()
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "A" and is_MAS_square(matrix, i, j):
                res += 1
    print(res)


part2()
