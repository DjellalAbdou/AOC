from collections import defaultdict
import functools

file = "input.txt"


def create_order_map():
    order_map = defaultdict(list)
    updates = []
    with open(file, "r") as f:
        is_orders = True
        for line in f:
            line = line.strip()
            if not line:
                is_orders = False
                continue
            if is_orders:
                before, after = line.split("|")
                order_map[before].append(after)
            else:
                updates.append(line.strip())
    f.close()
    return (order_map, updates)


def is_before(order_map, entry, checked_val, memo):
    if (entry, checked_val) in memo:
        return memo[(entry, checked_val)]

    check = False
    for next_val in order_map[entry]:
        if next_val == checked_val:
            memo[(entry, checked_val)] = True
            return True
        check = check and is_before(order_map, next_val, checked_val, memo)
    if check:
        memo[(entry, checked_val)] = True
    return check


def part1():
    order_map, updates = create_order_map()
    memo = {}
    res = 0
    for update in updates:
        splitted_update = update.split(",")
        is_ordered = True
        for i in range(len(splitted_update) - 1):
            current = splitted_update[i]
            for check_after in splitted_update[i + 1 :]:
                if is_ordered:
                    if not is_before(order_map, current, check_after, memo):
                        is_ordered = False
        if is_ordered:
            res += int(splitted_update[len(splitted_update) // 2])
    print(res)


def part1_optimized():
    rules = defaultdict(bool)
    is_rules = True
    res = 0

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                is_rules = False
                continue
            if is_rules:
                before, after = line.split("|")
                rules[(before, after)] = True
            else:
                splitted_update = line.split(",")
                is_ordered = True
                for i in range(len(splitted_update) - 1):
                    if not is_ordered:
                        break
                    current = splitted_update[i]
                    for check_after in splitted_update[i + 1 :]:
                        if rules[(check_after, current)]:
                            is_ordered = False
                            break
                if is_ordered:
                    res += int(splitted_update[len(splitted_update) // 2])
    f.close()
    print(res)


def order_and_get_element(rules, splitted_update):
    resulting_order = splitted_update.copy()
    # is_ordered = False
    # while not is_ordered:
    #     is_ordered = True
    #     for i in range(len(resulting_order) - 1):
    #         current = resulting_order[i]
    #         for j in range(i + 1, len(resulting_order)):
    #             check_after = resulting_order[j]
    #             if rules[(check_after, current)]:
    #                 is_ordered = False
    #                 resulting_order[i] = check_after
    #                 resulting_order[j] = current
    #                 break
    #         if not is_ordered:
    #             break
    order_list(rules, resulting_order)
    return int(resulting_order[len(resulting_order) // 2])


def order_list(rules, splitted_update):
    def compare(a, b):
        if rules[(b, a)]:
            return 1
        if rules[(a, b)]:
            return -1
        return 0

    splitted_update.sort(key=functools.cmp_to_key(compare))


def part2():
    rules = defaultdict(bool)
    is_rules = True
    res = 0

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                is_rules = False
                continue
            if is_rules:
                before, after = line.split("|")
                rules[(before, after)] = True
            else:
                splitted_update = line.split(",")
                is_ordered = True
                for i in range(len(splitted_update) - 1):
                    if not is_ordered:
                        break
                    current = splitted_update[i]
                    for check_after in splitted_update[i + 1 :]:
                        if rules[(check_after, current)]:
                            is_ordered = False
                            break
                if not is_ordered:
                    res += order_and_get_element(rules, splitted_update)
    f.close()
    print(res)


part2()
