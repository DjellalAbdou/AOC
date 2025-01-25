file = "input.txt"


def create_map():
    with open(file) as f:
        return [list(line.strip()) for line in f]


def get_region(value, row, col, matrix, visited, region_cells):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    edges = 0
    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[row]):
            edges += 1
            continue
        if (r, c) in visited:
            if visited[(r, c)] == value:
                continue
            edges += 1
            continue
        if matrix[r][c] == value:
            visited[(r, c)] = value
            region_cells.add((r, c))
            edges += get_region(value, r, c, matrix, visited, region_cells)
        else:
            edges += 1
    return edges


def part1():
    matrix = create_map()
    visited = {}
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row, col) not in visited:
                region_cells = set()
                region_cells.add((row, col))
                visited[(row, col)] = matrix[row][col]
                edges = get_region(
                    matrix[row][col], row, col, matrix, visited, region_cells
                )
                total += len(region_cells) * edges
    print(total)


def check_intervales(edges, border):
    row, col, dir_letter = border
    edges[(row, col, dir_letter)] = False
    if dir_letter == "U" or dir_letter == "D":
        if (row, col + 1, dir_letter) in edges:
            edges[(row, col, dir_letter)] = (row, col + 1, dir_letter)
        if (row, col - 1, dir_letter) in edges:
            edges[(row, col - 1, dir_letter)] = (row, col, dir_letter)
    else:
        if (row + 1, col, dir_letter) in edges:
            edges[(row, col, dir_letter)] = (row + 1, col, dir_letter)
        if (row - 1, col, dir_letter) in edges:
            edges[(row - 1, col, dir_letter)] = (row, col, dir_letter)


def get_region_with_full_edges(value, row, col, matrix, visited, region_cells, edges):
    directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
    for direction in directions:
        dr, dc, dir_letter = direction
        r, c = row + dr, col + dc
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[row]):
            check_intervales(edges, (row, col, dir_letter))
            continue
        if (r, c) in visited:
            if visited[(r, c)] == value:
                continue
            check_intervales(edges, (row, col, dir_letter))
            continue
        if matrix[r][c] == value:
            visited[(r, c)] = value
            region_cells.add((r, c))
            get_region_with_full_edges(
                value, r, c, matrix, visited, region_cells, edges
            )
        else:
            check_intervales(edges, (row, col, dir_letter))
    return


def part2():
    matrix = create_map()
    visited = {}
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row, col) not in visited:
                region_cells = set()
                region_cells.add((row, col))
                visited[(row, col)] = matrix[row][col]
                edges = {}
                get_region_with_full_edges(
                    matrix[row][col], row, col, matrix, visited, region_cells, edges
                )
                perimeter = sum(map(lambda x: 1 if not edges[x] else 0, edges))
                total += len(region_cells) * perimeter
    print(total)


part2()
