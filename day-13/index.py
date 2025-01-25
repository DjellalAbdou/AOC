import re
from typing import List, Tuple, Set

file = "input.txt"


def create_dataset():
    prizes = {}
    regex = re.compile(r"\d+")
    lines = []

    with open(file) as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines), 3):
        button_a = tuple(map(int, regex.findall(lines[i])))
        button_b = tuple(map(int, regex.findall(lines[i + 1])))
        prize = tuple(int(x) + 10000000000000 for x in regex.findall(lines[i + 2]))
        prizes[prize] = [button_a, button_b]

    return prizes


def check_prize_recursive(
    prize: Tuple[int, int],
    current_val: Tuple[int, int],
    tokens: int,
    press_a: int,
    press_b: int,
    results: List[int],
    visited: Set[Tuple[int, int]],
) -> None:
    goal = prize[0]
    button_a, button_b = prize[1]
    if current_val in visited:
        return

    visited.add(current_val)

    if current_val == goal:
        results.append(tokens)
        return

    if current_val[0] > goal[0] or current_val[1] > goal[1]:
        return

    if press_a <= 100:
        check_prize_recursive(
            prize,
            (current_val[0] + button_a[0], current_val[1] + button_a[1]),
            tokens + 3,
            press_a + 1,
            press_b,
            results,
            visited,
        )
    if press_b <= 100:
        check_prize_recursive(
            prize,
            (current_val[0] + button_b[0], current_val[1] + button_b[1]),
            tokens + 1,
            press_a,
            press_b + 1,
            results,
            visited,
        )


def check_prize(prize) -> int:
    goal = prize[0]
    button_a, button_b = prize[1]
    denuminator = button_a[0] * button_b[1] - button_a[1] * button_b[0]
    numerator = goal[0] * button_b[1] - goal[1] * button_b[0]
    if denuminator == 0 or numerator % denuminator != 0:
        return 0

    a_press = numerator // denuminator
    if a_press < 0:
        return 0
    numerator = goal[1] - a_press * button_a[1]
    denuminator = button_b[1]
    if denuminator == 0 or numerator % denuminator != 0:
        return 0
    b_press = numerator // denuminator
    if b_press < 0:
        return 0
    return a_press * 3 + b_press


def part2():
    prizes = create_dataset()
    total_tokens = 0
    for prize in prizes.items():
        total_tokens += check_prize(prize)

    print(total_tokens)
    return


part2()
