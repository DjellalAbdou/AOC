file = "input.txt"


def create_map():
    with open(file) as f:
        return [list(line.strip()) for line in f.readlines()]


def get_region(id, i, j, matrix, regions_map, current_region):
    if regions_map.get((i, j)):
        return 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nb_edges = 0
    for direction in directions:
        di, dj = direction
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= len(matrix) or nj >= len(matrix[i]):
            nb_edges += 1
            continue
        if matrix[ni][nj] == id:
            regions_map[(ni, nj)] = id
            current_region.add((ni, nj))
            nb_edges += get_region(id, ni, nj, matrix, regions_map, current_region)
        else:
            nb_edges += 1
        return nb_edges


def part1():
    matrix = create_map()
    regions_map = {}
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if regions_map.get((i, j)):
                continue
            current_region = set()
            current_region.add((i, j))
            nb_edges = get_region(
                matrix[i][j], i, j, matrix, regions_map, current_region
            )
            total += len(current_region) * nb_edges
    print(total)


part1()
