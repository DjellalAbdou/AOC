import re
file = "input.txt"

def multiply_command(command: str):
  numbers = list(map(int, re.findall(r'\d+', command)))
  return numbers[0] * numbers[1]

def part1():
  with open(file, "r") as f:
    res = sum(
        multiply_command(match)
        for line in f
        for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
      )
    print(res)


def part2():
  with open(file, "r") as f:
    enabled = True
    res = 0
    for line in f:
      for match in re.findall(r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", line):
        if match == "don't()":
          enabled = False
        elif match == "do()":
          enabled = True
        elif enabled:
          res += multiply_command(match)
    
    print(res)

part2()
