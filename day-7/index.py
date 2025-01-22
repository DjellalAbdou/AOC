file = "input.txt"


def is_test_possible(test_val, values, res):
    is_possible = False
    for op1 in ["+", "x", "||"]:
        if op1 == "+":
            if len(values) == 1:
                is_possible = is_possible | (test_val == res + values[0])
            else:
                is_possible = is_possible | is_test_possible(
                    test_val, values[1:], res + values[0]
                )
                if is_possible:
                    return is_possible
        elif op1 == "x":
            if len(values) == 1:
                is_possible = is_possible | (test_val == res * values[0])
            else:
                is_possible = is_possible | is_test_possible(
                    test_val, values[1:], res * values[0]
                )
                if is_possible:
                    return is_possible
        # This is for part 2
        elif op1 == "||":
            if len(values) == 1:
                is_possible = is_possible | (test_val == int(str(res) + str(values[0])))
            else:
                is_possible = is_possible | is_test_possible(
                    test_val, values[1:], int(str(res) + str(values[0]))
                )
                if is_possible:
                    return is_possible
    return is_possible


def part1():
    count = 0
    with open(file, "r") as f:
        for line in f:
            test_val, values = line.split(":")
            test_val = int(test_val)
            values = list(map(int, values.strip().split(" ")))
            if is_test_possible(test_val, values[1:], values[0]):
                count += test_val
    print(count)


part1()
