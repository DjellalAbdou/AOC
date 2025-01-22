file = "./input.txt"

def part1():
  res = 0
  list1 = []
  list2 = []

  with open(file, "r") as f:
      for line in f:
          tempLine = line.strip().split("   ")
          list1.append(int(tempLine[0]))
          list2.append(int(tempLine[1]))

  list1.sort()
  list2.sort()

  for i in range(len(list1)):
      res += abs(list1[i] - list2[i])

  print(res)

def part2():
  res = 0
  list1 = []
  occurence_of_elem = {}

  with open(file, "r") as f:
      for line in f:
          tempLine = line.strip().split("   ")
          list1.append(int(tempLine[0]))
          tempElem = int(tempLine[1])
          if occurence_of_elem.get(tempElem) is not None:
              occurence_of_elem[tempElem] += 1
          else:
              occurence_of_elem[tempElem] = 1
  for i in range(len(list1)):
      if occurence_of_elem.get(list1[i]) is not None:
          res += list1[i] * occurence_of_elem[list1[i]]

  print(res)

part2()
