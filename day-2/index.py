file = "./input.txt"

def is_sorted_and_safe(arr, direction = "asc"):
  for a, b in zip(arr, arr[1:]):
    if (direction == "asc" and a >= b) or (direction == "desc" and a <= b):
      return False
    if abs(a - b) > 3:
        return False
  return True

def part1():
  with open(file, "r") as f:
    res = [is_sorted_and_safe(line) or is_sorted_and_safe(line, "desc") for line in (list(map(int, line.strip().split(" "))) for line in f)].count(True)
    print(res)

def soft_is_sorted_and_safe(arr, direction = "asc"):
  if is_sorted_and_safe(arr, direction):
    return True
  for i in range(len(arr)):
    temp = arr.copy()
    temp.pop(i)
    if is_sorted_and_safe(temp, direction):
      return True

def part2():
  with open(file, "r") as f:
    res = [soft_is_sorted_and_safe(line) or soft_is_sorted_and_safe(line, "desc") for line in (list(map(int, line.strip().split(" "))) for line in f)].count(True)
    print(res)

part2()
