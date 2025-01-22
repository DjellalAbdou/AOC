file = "input.txt"


def create_map():
    matrix = []
    row = 0
    start_index = (0, 0)
    with open(file, "r") as f:
        for line in f:
            line = list(line.strip())
            matrix.append(line)
            if "^" in line:
                start_index = (row, line.index("^"))
            row += 1
    return (matrix, start_index)


def move_forward(row, col, direction):
    if direction == "N":
        return (row - 1, col)
    if direction == "S":
        return (row + 1, col)
    if direction == "E":
        return (row, col + 1)
    if direction == "W":
        return (row, col - 1)


def turn_right(direction):
    if direction == "N":
        return "E"
    if direction == "S":
        return "W"
    if direction == "E":
        return "S"
    if direction == "W":
        return "N"


def is_getting_out_of_bounds(row, col, matrix, direction):
    return (
        direction == "N"
        and row == 0
        or direction == "S"
        and row == len(matrix) - 1
        or direction == "E"
        and col == len(matrix[0]) - 1
        or direction == "W"
        and col == 0
    )


def part1(route_map, row, col):
    memo = {}
    memo[(row, col)] = True  # Add the starting point
    direction = "N"
    while not is_getting_out_of_bounds(row, col, route_map, direction):
        mv_row, mv_col = move_forward(row, col, direction)
        if route_map[mv_row][mv_col] == "#":
            direction = turn_right(direction)
            continue
        row, col = mv_row, mv_col
        memo[(row, col)] = True
    return memo


def is_path_infinit(row, col, route_map, direction):
    memo = {}
    used_row = row
    used_col = col
    used_direction = direction

    memo[(used_row, used_col, used_direction)] = True
    is_infinite = False
    while not is_getting_out_of_bounds(used_row, used_col, route_map, used_direction):
        mv_row, mv_col = move_forward(used_row, used_col, used_direction)
        if route_map[mv_row][mv_col] == "#":
            used_direction = turn_right(used_direction)
            continue
        used_row, used_col = mv_row, mv_col
        if (used_row, used_col, used_direction) in memo:
            is_infinite = True
            break
        memo[(used_row, used_col, used_direction)] = True
    return is_infinite


def part2():
    possible_infinite_loops = 0
    route_map, (row, col) = create_map()
    possible_spots = part1(route_map, row, col)
    direction = "N"
    for i in range(len(route_map)):
        for j in range(len(route_map[0])):
            temp = route_map[i][j]
            if temp == "#" or temp == "^" or (i, j) not in possible_spots:
                continue
            route_map[i][j] = "#"
            if is_path_infinit(row, col, route_map, direction):
                possible_infinite_loops += 1
            route_map[i][j] = temp
    print(possible_infinite_loops)


part2()
