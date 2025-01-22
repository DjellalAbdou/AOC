file = "input.txt"


def create_stone_list():
    with open(file) as f:
        return list(map(int, f.readline().strip().split(" ")))


def part1():
    stone_list = create_stone_list()
    temp_list = []
    for i in range(0, 75):
        for j in range(len(stone_list)):
            if stone_list[j] == 0:
                temp_list.append(1)
                continue
            number_as_string = str(stone_list[j])
            if len(number_as_string) % 2 == 0:
                temp_list.append(int(number_as_string[0 : len(number_as_string) // 2]))
                temp_list.append(int(number_as_string[len(number_as_string) // 2 :]))
                continue
            temp_list.append(stone_list[j] * 2024)
        stone_list = temp_list
        temp_list = []

    print(len(stone_list))


# blink is like depth in the recursion
def transform_stone(stone, blink, memo):
    if (blink, stone) in memo:
        return memo[(blink, stone)]
    if blink == 75:
        return 1
    number_as_string = str(stone)
    if stone == 0:
        res = transform_stone(1, blink + 1, memo)

    elif len(number_as_string) % 2 == 0:
        res = transform_stone(
            int(number_as_string[0 : len(number_as_string) // 2]), blink + 1, memo
        ) + transform_stone(
            int(number_as_string[len(number_as_string) // 2 :]), blink + 1, memo
        )
    else:
        res = transform_stone(stone * 2024, blink + 1, memo)

    memo[(blink, stone)] = res
    return res


def part2():
    stone_list = create_stone_list()
    res = 0
    memo = {}
    for stone in stone_list:
        res += transform_stone(stone, 0, memo)

    print(res)


part2()
