from collections import defaultdict

file = "input.txt"


def get_antinodes(pos1, pos2):
    # each two positions will produce 2 antinodes
    difference = (pos1[0] - pos2[0], pos1[1] - pos2[1])
    antinode1 = (pos1[0] + difference[0], pos1[1] + difference[1])
    antinode2 = (pos2[0] - difference[0], pos2[1] - difference[1])

    return (antinode1, antinode2)


def create_map():
    antena_map = defaultdict(list)
    max_row = 0
    max_col = 0
    with open(file, "r") as f:
        cpt = 0
        for line in f:
            pos_array = list(line.strip())
            max_col = len(pos_array)
            for i in range(len(pos_array)):
                if pos_array[i] != ".":
                    antena_map[pos_array[i]].append((cpt, i))
            cpt += 1
        max_row = cpt
    return (antena_map, max_row, max_col)


def part1():
    antena_map, max_row, max_col = create_map()
    uniquePos = set()
    for key, matrix_positions in antena_map.items():
        for i in range(len(matrix_positions)):
            for compare_pos in matrix_positions[i + 1 :]:
                antinodes = get_antinodes(matrix_positions[i], compare_pos)
                for antinode in antinodes:
                    if (
                        antinode[0] >= 0
                        and antinode[0] < max_row
                        and antinode[1] >= 0
                        and antinode[1] < max_col
                    ):
                        uniquePos.add(antinode)
    print(len(uniquePos))


def get_antinodes_with_resonant(pos1, pos2, max_row, max_col):
    antinodes = [pos1, pos2]
    current_node = (pos1[0], pos1[1])
    difference = (pos1[0] - pos2[0], pos1[1] - pos2[1])
    while True:
        current_node = (
            current_node[0] + difference[0],
            current_node[1] + difference[1],
        )
        if (
            current_node[0] < 0
            or current_node[0] >= max_row
            or current_node[1] < 0
            or current_node[1] >= max_col
        ):
            break
        antinodes.append(current_node)

    while True:
        current_node = (
            current_node[0] - difference[0],
            current_node[1] - difference[1],
        )
        if (
            current_node[0] < 0
            or current_node[0] >= max_row
            or current_node[1] < 0
            or current_node[1] >= max_col
        ):
            break
        antinodes.append(current_node)
    return antinodes


def part2():
    antenna_map, max_row, max_col = create_map()
    uniquePos = set()
    for key, matrix_positions in antenna_map.items():
        for i in range(len(matrix_positions)):
            for compare_pos in matrix_positions[i + 1 :]:
                antinodes = get_antinodes_with_resonant(
                    matrix_positions[i], compare_pos, max_row, max_col
                )
                for antinode in antinodes:
                    uniquePos.add(antinode)
    print(len(uniquePos))


part2()
