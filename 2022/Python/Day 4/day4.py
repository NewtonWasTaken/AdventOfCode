input = open("input.txt")
text = [y.split("-") for x in [i.split(",") for i in input.read().splitlines()] for y in x]
result = 0
result2 = 0
for x in range(len(text)):
    if (x + 1) % 2 == 0:
        first_set = set(list(range(int(text[x-1][0]), int(text[x-1][1]) + 1)))
        second_set = set(list(range(int(text[x][0]), int(text[x][1]) + 1)))
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            result += 1
        if len(first_set.intersection(second_set)) != 0:
            result2 += 1
print(result)
print(result2)