input = open("input.txt")
text = [i.split(",") for i in input.read().splitlines()]
text2 = [y.split("-") for x in text for y in x]
result = 0
for x in range(len(text2)):
    if (x + 1) % 2 == 0:
        for y in range(len(text2[x])):
            if y == 1:
                first_set = set(list(range(int(text2[x-1][y-1]), int(text2[x-1][y]) + 1)))
                second_set = set(list(range(int(text2[x][y-1]), int(text2[x][y]) + 1)))
                if first_set.issubset(second_set) or second_set.issubset(first_set):
                    result += 1
        first_set = set()
        second_set = set()
print(result)
result = 0
for x in range(len(text2)):
    if (x + 1) % 2 == 0:
        for y in range(len(text2[x])):
            if y == 1:
                first_set = set(list(range(int(text2[x-1][y-1]), int(text2[x-1][y]) + 1)))
                second_set = set(list(range(int(text2[x][y-1]), int(text2[x][y]) + 1)))
                if len(first_set.intersection(second_set)) != 0 or len(second_set.intersection(first_set)) != 0:
                    result += 1
        first_set = set()
        second_set = set()
print(result)